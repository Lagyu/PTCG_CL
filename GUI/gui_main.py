from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty,BoundedNumericProperty
from kivy.properties import StringProperty
from GUI.dragrecognizer import DragRecognizer
from GUI.hoverbehavior import HoverBehavior
from kivy.factory import Factory
from kivy.base import runTouchApp
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, BorderImage

Factory.register('HoverBehavior', HoverBehavior)

ids_on_hover = []


class Board(BoxLayout):
    def __init__(self,*args,**kwargs):
        super(Board, self).__init__(*args, **kwargs)
        global root_board
        root_board = self

class OppBPArea(BoxLayout):
    pass


class OppBPMarginLabelLeft(Label):
    pass


class OppBPGXMarker(Label):
    pass


class OppBPPrizePile(Label):
    pass


class OppBPBattlePokemonBoxLayout(Label):
    pass


class OppBPDeck(Label):
    pass


class OppBPMarginLabelRIght(Label):
    pass


class OppBenchArea(BoxLayout):
    pass


class OppBenchMarginLabelLeft(Label):
    pass


class OppBenchBenchPokemonFloatLayoutContainer(FloatLayout):
    pass


class OppBenchBenchPokemonInnerBoxLayout(BoxLayout):
    pass


class OppBenchBenchPokemonIndividualFloatLayoutContainer(FloatLayout):
    pass


class OppBenchBenchPokemonIndividualBoxLayout(DragBehavior, HoverBehavior, BoxLayout):
    name = StringProperty("")
    is_on_hover = BooleanProperty(False)
    origin_pos_x = BoundedNumericProperty(0)
    origin_pos_y = BoundedNumericProperty(0)

    def __init__(self, **args):
        super(OppBenchBenchPokemonIndividualBoxLayout, self).__init__()
        self.is_on_hover = False

    def on_enter(self):
        global ids_on_hover
        ids_on_hover.append(self.name)
        print(ids_on_hover)
        self.is_on_hover = True
        with self.canvas.after:
            BorderImage(source="Transparent_shadow32.png", pos=(self.x - self.width * 0.2, self.y - self.height * 0.2),
                        size=(self.width * 1.35, self.height * 1.35), index=1000)

    def on_leave(self):
        # ids_on_hover.remove(self.name)
        obj_name = self.name
        global ids_on_hover
        ids_on_hover = [value for value in ids_on_hover if value != obj_name]  # remove all from list
        print(ids_on_hover)
        self.is_on_hover = False
        #        print(self.name)
        self.canvas.after.clear()

    def on_touch_down(self, touch):
        super(OppBenchBenchPokemonIndividualBoxLayout, self).on_touch_down(touch)
        self.canvas.after.clear()
        self.origin_pos_x = self.x
        self.origin_pos_y = self.y
        if self.is_on_hover:
            ChildrenList = []
            for i in range(len(self.parent.children)):
                ChildrenList.append(self.parent.children[i].name)
            print(ChildrenList)
            print(root_board.ids["box1_id"].name)  # idへのアクセスは、最上位のウィジェットから行う
    
    def on_touch_up(self, touch):
        super(OppBenchBenchPokemonIndividualBoxLayout, self).on_touch_up(touch)
        self.x = self.origin_pos_x
        self.y = self.origin_pos_y
        if self.is_on_hover:
            print("piyo")


class OppBenchTrashPile(Label):
    pass


class OppBenchMarginLabelLeft(Label):
    pass


class OppHandArea(BoxLayout):
    pass


class OppHandMarginLabelLeft(Label):
    pass


class OppHandHand(Label):
    pass


class OppHandMarginLabelRight(Label):
    pass


class MyBPArea(BoxLayout):
    pass


class MyBPMarginLabelLeft(Label):
    pass


class MyBPGXMarker(Label):
    pass


class MyBPPrizePile(Label):
    pass


class MyBPBattlePokemonBoxLayout(Label):
    pass


class MyBPDeck(Label):
    pass


class MyBPMarginLabelRIght(Label):
    pass


class MyBenchArea(BoxLayout):
    pass


class MyBenchMarginLabelLeft(Label):
    pass


class MyBenchBenchPokemonBoxLayout(Label):
    pass


class MyBenchTrashPile(Label):
    pass


class MyBenchMarginLabelLeft(Label):
    pass


class MyHandArea(BoxLayout):
    pass


class MyHandMarginLabelLeft(Label):
    pass


class MyHandHand(Label):
    pass


class MyHandMarginLabelRight(Label):
    pass


class DragHandCard(Widget, DragBehavior, HoverBehavior):
    def on_touch_down(self, touch):
        print(touch)


class BoardAreaContainer(HoverBehavior, BoxLayout):

    name = StringProperty("")

    def __init__(self, *args, **kwargs):
        super(BoardAreaContainer, self).__init__(**kwargs)

    def hand(self):
        print(self.ids)

    def on_enter(self):
        super(BoardAreaContainer, self).on_enter()
        self.hand()


'''
class DraggableImage(DragBehavior, HoverBehavior, Image):

    name = StringProperty("")
    is_on_hover = BooleanProperty(False)
    origin_pos_x = BoundedNumericProperty(0)
    origin_pos_y = BoundedNumericProperty(0)

    def __init__(self, **args):
        super(DraggableImage, self).__init__(**args)
        self.is_on_hover = False

    def on_enter(self):
        self.is_on_hover = True
        global ids_on_hover
        ids_on_hover.append(self.name)
        print(ids_on_hover)
        with self.canvas.after:
            BorderImage(source="Transparent_shadow32.png", pos=(self.x-self.width*0.2, self.y-self.height*0.2), size=(self.width*1.4, self.height*1.4), index = 1000)

    def on_leave(self):
        # ids_on_hover.remove(self.name)
        obj_name = self.name
        global ids_on_hover
        ids_on_hover = [value for value in ids_on_hover if value != obj_name]
        print(ids_on_hover)
        self.is_on_hover = False
#        print(self.name)
        self.canvas.after.clear()

    def on_touch_down(self, touch):
        super(DraggableImage, self).on_touch_down(touch)
        self.canvas.after.clear()
        self.origin_pos_x = self.x
        self.origin_pos_y = self.y
        if self.is_on_hover:
            ChildrenList = []
            for i in range(len(self.parent.children)):
                ChildrenList.append(self.parent.children[i].name)
            print(ChildrenList)

    def on_touch_up(self, touch):
        super(DraggableImage, self).on_touch_up(touch)
        self.x = self.origin_pos_x
        self.y = self.origin_pos_y
        if self.is_on_hover:
            print(self.parent.children)
'''


class BattleboardApp(App):
    def __init__(self, **kwargs):
        super(BattleboardApp, self).__init__(**kwargs)

    def build(self):
        return Board()


if __name__ == '__main__':
    BattleboardApp().run()
