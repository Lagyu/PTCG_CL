from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.base import runTouchApp

class HoverBehavior(object):
    """Hover behavior.
    :Events:
        `on_enter`
            Fired when mouse enter the bbox of the widget.
        `on_leave`
            Fired when the mouse exit the widget
    """

    hovered = BooleanProperty(False)
    border_point = ObjectProperty(None)
    '''Contains the last relevant point received by the Hoverable. This can
    be used in `on_enter` or `on_leave` in order to know where was dispatched the event.
    '''

    def __init__(self, **kwargs):
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return # do proceed if I'm not displayed <=> If have no parent
        pos = args[1]
        # Next line to_widget allow to compensate for relative layout
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            # We have already done what was needed
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_enter(self):
        pass

    def on_leave(self):
        pass


Factory.register('HoverBehavior', HoverBehavior)


class DragHandCard(Widget, DragBehavior, HoverBehavior):
    def on_touch_down(self, touch):
        print(touch)


defpos_x = 0
defpos_y = 0


class MyPaintWidget(Widget, DragBehavior):
    def on_touch_down(self, touch):
        global defpos_x
        defpos_x = touch.x
        global defpos_y
        defpos_y = touch.y
        print(touch)


class BattleboardApp(App):
    def __init__(self, **kwargs):
        super(BattleboardApp, self).__init__(**kwargs)
        self.title = "ぴよ"

    def build(self):
        return MyPaintWidget()


if __name__ == '__main__':
    BattleboardApp().run()

