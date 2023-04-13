from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.image import Image as CoreImage
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty
from kivy.core.window import Window

class MenuScreen(Screen):
    pass

class DialogueScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'spacebar' and self.manager.current == "dialogue":
            self.manager.current = "end"

class EndScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    FONT_SIZE = StringProperty("20dp")


class TheLabApp(App):
    def build(self):
        return MyScreenManager()

if __name__ == "__main__":
    TheLabApp().run()
