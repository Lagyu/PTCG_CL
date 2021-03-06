from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
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
from ptcgcl import Board_changer
from kivy.uix.behaviors import ButtonBehavior

Factory.register('HoverBehavior', HoverBehavior)

opp_bp_bp_on_hover = ""
opp_bench_bench_on_hover = ""
my_bp_bp_on_hover = ""
my_bench_bench_on_hover = ""
holding_now = ""


class MainMenu(ModalView):
    pass


class MainMenuContents(BoxLayout):
    pass


class Board(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Board, self).__init__(*args, **kwargs)
        global root_board
        root_board = self


class ChooseModal(ModalView):
    pass


class ModalInnerBox(BoxLayout):
    pass


class CardsChooseFrom(BoxLayout):
    def __init__(self, **kwargs):
        super(CardsChooseFrom, self).__init__()

    def load_all(self, from_key: str, number_take: int, filter_supertype="any", filter_subtype="any"):
        # 未実装、returnはlistで
        for i in range(len(Board_changer.Board_CL().board_dic.index(from_key))):
            img_i = Board_changer.Board_CL()[Board_changer.Board_CL().board_dic.index(from_key), i, "id"] + ".png"
            self.add_widget(ChooseModalItemCards(source=img_i, id=img_i, name=str(i)))

    def load_pokemon(self, from_key: str, number_take: int, filter_supertype="any", filter_subtype="any", filter_type="any", name_list=[], filter_hp_min=0, filter_hp_max=0, filter_retreat_cost_min=0, filter_retreat_cost_max=1000):
        # 未実装
        for i in range(len(Board_changer.Board_CL().board_dic.index(from_key))):
            img_i = Board_changer.Board_CL()[Board_changer.Board_CL().board_dic.index(from_key), i, "id"] + ".png"
            self.add_widget(ChooseModalItemCards(source=img_i, id=img_i, name=str(i)))

    def load_energy(self, from_key: str, number_take: int, filter_supertype="any", filter_subtype="any", filter_type=[], name_list=[]):
        # 未実装
        for i in range(len(Board_changer.Board_CL().board_dic.index(from_key))):
            img_i = Board_changer.Board_CL()[Board_changer.Board_CL().board_dic.index(from_key), i, "id"] + ".png"
            self.add_widget(ChooseModalItemCards(source=img_i, id=img_i, name=str(i)))


class ChooseModalItemCards(ButtonBehavior, Image):
    def on_press(self):
        super(ChooseModalItemCards, self).on_press()
        # ここに自身のon_pressを取り除き、自身の内容をChooseModalItemCardsChosenに入れるって書く
        pass


class ChooseModalItemCardsChosen(ButtonBehavior, Image):
    def on_press(self):
        super(ChooseModalItemCards, self).on_press()
        # ここに自身を取り除き、上のやつにon_pressを戻すって書く
        pass


class OppBPArea(BoxLayout):
    pass


class OppBPMarginLabelLeft(Label):
    pass


class OppBPGXMarker(Label):
    pass


class OppBPPrizePile(Label):
    pass


class OppBPBattlePokemonBoxLayout(HoverBehavior, BoxLayout):
    pass


class OppBPInPlayCards(HoverBehavior, BoxLayout):
    pass


class OppBPDeck(Label):
    pass


class OppBPMarginLabelRight(Label):
    pass


class OppBenchArea(BoxLayout):
    pass


class OppBenchMarginLabelLeft(Label):
    pass


class OppBenchBenchPokemonFloatLayoutContainer(FloatLayout):
    pass


class OppBenchBenchPokemonInnerBoxLayout(BoxLayout):
    def on_touch_up(self, touch):
        super(OppBenchBenchPokemonInnerBoxLayout, self).on_touch_down(touch)
        self.clear_widgets()
        Board_changer.Board_CL()[Board_changer.Board_CL().board_dic.index("POKEMON_P_1"), 0] = [{'artist': 'Mizue', 'attacks': [{'convertedEnergyCost': 1, 'cost': ['Colorless'], 'damage': '', 'name': 'Sharp Blade Quill', 'text': "This attack does 20 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)"}, {'convertedEnergyCost': 3, 'cost': ['Grass', 'Colorless', 'Colorless'], 'damage': '50+', 'name': 'Leaf Blade', 'text': 'Flip a coin. If heads, this attack does 20 more damage.'}], 'evolvesFrom': 'Rowlet', 'hp': '80', 'id': 'sm1-10', 'imageUrl': 'https://images.pokemontcg.io/sm1/10.png', 'imageUrlHiRes': 'https://images.pokemontcg.io/sm1/10_hires.png', 'name': 'Dartrix', 'nationalPokedexNumber': 723, 'number': '10', 'rarity': 'Uncommon', 'retreatCost': ['Colorless'], 'series': 'Sun & Moon', 'set': 'Sun & Moon', 'setCode': 'sm1', 'subtype': 'Stage 1', 'supertype': 'Pokémon', 'types': ['Grass'], 'weaknesses': [{'type': 'Fire', 'value': '×2'}]}]
        Board_changer.Board_CL()[Board_changer.Board_CL().board_dic.index("POKEMON_P_1"), 1] = [{'artist': 'Mizue', 'attacks': [{'convertedEnergyCost': 1, 'cost': ['Colorless'], 'damage': '', 'name': 'Sharp Blade Quill', 'text': "This attack does 20 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)"}, {'convertedEnergyCost': 3, 'cost': ['Grass', 'Colorless', 'Colorless'], 'damage': '50+', 'name': 'Leaf Blade', 'text': 'Flip a coin. If heads, this attack does 20 more damage.'}], 'evolvesFrom': 'Rowlet', 'hp': '80', 'id': 'sm1-10', 'imageUrl': 'https://images.pokemontcg.io/sm1/10.png', 'imageUrlHiRes': 'https://images.pokemontcg.io/sm1/10_hires.png', 'name': 'Dartrix', 'nationalPokedexNumber': 723, 'number': '10', 'rarity': 'Uncommon', 'retreatCost': ['Colorless'], 'series': 'Sun & Moon', 'set': 'Sun & Moon', 'setCode': 'sm1', 'subtype': 'Stage 1', 'supertype': 'Pokémon', 'types': ['Grass'], 'weaknesses': [{'type': 'Fire', 'value': '×2'}]}]
        for i in range(1, len(Board_changer.Board_CL()[Board_changer.Board_CL().board_dic.index("POKEMON_P_1")])):
            if Board_changer.Board_CL()[Board_changer.Board_CL().board_dic.index("POKEMON_P_1"), i] == []:
                break
            name_i = "POKEMON_P_1_"+str(i)
            box = OppBenchBenchPokemonIndividualBoxLayout(id=name_i, name=name_i, card_text_list=Board_changer.Board_CL()[Board_changer.Board_CL().board_dic.index("POKEMON_P_1"), i])
            self.add_widget(box)
            img_i = Board_changer.Board_CL()[Board_changer.Board_CL().board_dic.index("POKEMON_P_1"), i, -1, "id"] + ".png"
            self.children[i-1].add_widget(Image(source=img_i, name=img_i, id=img_i))


class OppBenchBenchPokemonIndividualBoxLayout(DragBehavior, HoverBehavior, BoxLayout):
    name = StringProperty("")
    is_on_hover = BooleanProperty(False)
    origin_pos_x = BoundedNumericProperty(0)
    origin_pos_y = BoundedNumericProperty(0)

    def __init__(self, **args):
        super(OppBenchBenchPokemonIndividualBoxLayout, self).__init__()
        self.is_on_hover = False
    def on_enter(self):
        global opp_bench_bench_on_hover
        opp_bench_bench_on_hover = self.name
        print(opp_bench_bench_on_hover)
        self.is_on_hover = True
        with self.canvas.after:
            BorderImage(source="Transparent_shadow32.png", pos=(self.x - self.width * 0.2, self.y - self.height * 0.2),
                        size=(self.width * 1.35, self.height * 1.35), index=1000)

    def on_leave(self):
        # ids_on_hover.remove(self.name)
        global opp_bench_bench_on_hover
        opp_bench_bench_on_hover = ""
        self.is_on_hover = False
        #        print(self.name)
        self.canvas.after.clear()

    def on_touch_down(self, touch):
        super(OppBenchBenchPokemonIndividualBoxLayout, self).on_touch_down(touch)
        self.canvas.after.clear()
        self.origin_pos_x = self.x
        self.origin_pos_y = self.y
        if self.is_on_hover:
            '''
            ChildrenList = []
            for i in range(len(self.parent.children)):
                ChildrenList.append(self.parent.children[i].name)
            print(ChildrenList)
            '''
            # print(root_board.ids[self.name].name)  # idへのアクセスは、最上位のウィジェットから行う

    def on_touch_up(self, touch):
        super(OppBenchBenchPokemonIndividualBoxLayout, self).on_touch_up(touch)
        if self.origin_pos_x == 0 and self.origin_pos_y == 0:
            pass
        else:
            self.x = self.origin_pos_x
            self.y = self.origin_pos_y
            if self.is_on_hover:
                pass
                # print(root_board.ids[self.name].name)


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


class MyBPMarginLabelRight(Label):
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


class MyHandFloatLayoutContainer(FloatLayout):
    pass


class MyHandHand(BoxLayout):
    def on_touch_up(self, touch):
        super(MyHandHand, self).on_touch_down(touch)
        # Board_changer.Board_CL()[Board_changer.Board_CL().board_dic.index("HAND_0")] = [{'artist': 'Mizue', 'attacks': [{'convertedEnergyCost': 1, 'cost': ['Colorless'], 'damage': '', 'name': 'Sharp Blade Quill', 'text': "This attack does 20 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)"}, {'convertedEnergyCost': 3, 'cost': ['Grass', 'Colorless', 'Colorless'], 'damage': '50+', 'name': 'Leaf Blade', 'text': 'Flip a coin. If heads, this attack does 20 more damage.'}], 'evolvesFrom': 'Rowlet', 'hp': '80', 'id': 'sm1-10', 'imageUrl': 'https://images.pokemontcg.io/sm1/10.png', 'imageUrlHiRes': 'https://images.pokemontcg.io/sm1/10_hires.png', 'name': 'Dartrix', 'nationalPokedexNumber': 723, 'number': '10', 'rarity': 'Uncommon', 'retreatCost': ['Colorless'], 'series': 'Sun & Moon', 'set': 'Sun & Moon', 'setCode': 'sm1', 'subtype': 'Stage 1', 'supertype': 'Pokémon', 'types': ['Grass'], 'weaknesses': [{'type': 'Fire', 'value': '×2'}]}, {'artist': 'Mizue', 'attacks': [{'convertedEnergyCost': 1, 'cost': ['Colorless'], 'damage': '', 'name': 'Sharp Blade Quill', 'text': "This attack does 20 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)"}, {'convertedEnergyCost': 3, 'cost': ['Grass', 'Colorless', 'Colorless'], 'damage': '50+', 'name': 'Leaf Blade', 'text': 'Flip a coin. If heads, this attack does 20 more damage.'}], 'evolvesFrom': 'Rowlet', 'hp': '80', 'id': 'sm1-10', 'imageUrl': 'https://images.pokemontcg.io/sm1/10.png', 'imageUrlHiRes': 'https://images.pokemontcg.io/sm1/10_hires.png', 'name': 'Dartrix', 'nationalPokedexNumber': 723, 'number': '10', 'rarity': 'Uncommon', 'retreatCost': ['Colorless'], 'series': 'Sun & Moon', 'set': 'Sun & Moon', 'setCode': 'sm1', 'subtype': 'Stage 1', 'supertype': 'Pokémon', 'types': ['Grass'], 'weaknesses': [{'type': 'Fire', 'value': '×2'}]}]
        self.clear_widgets()
        for i in range(len(Board_changer.Board_CL()[Board_changer.Board_CL().board_dic.index("HAND_0")])):
            if not Board_changer.Board_CL()[Board_changer.Board_CL().board_dic.index("HAND_0"), i]:
                break
            name_i = "HAND_0_"+str(i)
            try:
                img_i = "images\\"+Board_changer.Board_CL()[Board_changer.Board_CL().board_dic.index("HAND_0"), i, "id"] + ".png"
                hand_i = MyHandHandIndividualCard(id=name_i, name=name_i, source=img_i)
                self.add_widget(hand_i)
            except FileNotFoundError:
                print("Error detected. look into the current directory;")
                img_i = Board_changer.Board_CL()[Board_changer.Board_CL().board_dic.index("HAND_0"), i, "id"] + ".png"
                hand_i = MyHandHandIndividualCard(id=name_i, name=name_i, source=img_i)
                self.add_widget(hand_i)

class MyHandHandIndividualCard(DragBehavior, HoverBehavior, Image):
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