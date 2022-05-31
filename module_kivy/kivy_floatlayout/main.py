from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout


class MyW(FloatLayout):
    pass


class MyApp(App):
    def build(self):
        app_root = MyW()
        return app_root


if __name__ == "__main__":
    MyApp().run()
