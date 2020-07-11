from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.clock import Clock


class MyW(AnchorLayout):
    pass


class MyApp(App):
    def build(self):
        return MyW()


if __name__ == '__main__':
    MyApp().run()

