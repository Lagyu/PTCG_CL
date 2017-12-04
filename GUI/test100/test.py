from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.event import EventDispatcher
from kivy.lang import Builder

Builder.load_string("""
<RootWidget>:
    cols: 2
    Label:
        text: "Attribute a:"
    Label:
        text: root.data_model.a
    Label:
        text: "Attribute b:"
    Label:
        text: root.data_model.b
    Label:
        text: "Attribute c:"
    Label:
        text: root.data_model.c
    Button:
        text: "Make data_model.a longer"
        on_press: root.button_press()
    Button:
        text: "Make data_model.b shorter"
        on_press: root.button_press2()
""")


class DataModel(EventDispatcher):
    a = StringProperty('')
    b = StringProperty('')
    c = StringProperty('')

    def __init__(self, *args, **kwargs):
        super(DataModel, self).__init__(*args, **kwargs)
        self.a = 'This is a'
        self.b ='This is b'
        self.bind(a=self.set_c)
        self.bind(b=self.set_c)

    def set_c(self, instance, value):
        self.c = self.a + ' and ' + self.b

class RootWidget(GridLayout):
    data_model = ObjectProperty(DataModel())

    def button_press(self, *args):
        self.data_model.a = 'This is a and it is really long now'
        print(self.data_model.c)

    def button_press2(self, *args):
        self.data_model.b = 'B'
        print(self.data_model.c)

class TestApp(App):
    def build(self):
        return RootWidget()

app = TestApp()
app.run()