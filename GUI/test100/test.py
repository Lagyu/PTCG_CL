from kivy.app import App
from kivy.uix.behaviors import DragBehavior
from kivy.uix.image import Image

class DraggableImage(DragBehavior, Image):
    def on_touch_down(self, touch):  # without this, Image is always draggable.
        print("This is test")

class TestApp(App):
    def build(self):
        pass

if __name__ == '__main__':
    TestApp().run()