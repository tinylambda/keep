from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout


class MyW(FloatLayout):
    pass


class MyApp(App):
    def build(self):
        return MyW()


if __name__ == "__main__":
    MyApp().run()
