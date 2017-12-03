from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from GUI.dragrecognizer import DragRecognizer
from GUI.hoverbehavior import HoverBehavior
from kivy.factory import Factory
from kivy.base import runTouchApp
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line

Factory.register('HoverBehavior', HoverBehavior)


class DragHandCard(Widget, DragBehavior, HoverBehavior):
    def on_touch_down(self, touch):
        print(touch)


class DraggableImage(DragBehavior, Image):

    name = StringProperty("")
    is_on_hover = BooleanProperty(False)
    source_file = StringProperty("")

    def __init__(self, **args):
        super(DraggableImage, self).__init__(**args)
        self.source_file = ""
        self.is_on_hover = False

    def on_enter(self):
        self.source_file = self.source
        self.is_on_hover = True

    def on_leave(self):
        self.source = self.source_file
        self.is_on_hover = False

    def on_touch_up(self, touch):
        super(DraggableImage, self).on_touch_up(touch)
        print(self.name)


class BattleboardApp(App):
    def build(self):
        pass


if __name__ == '__main__':
    BattleboardApp().run()
