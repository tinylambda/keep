from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class MyW(GridLayout):
    pass


class MyApp(App):
    def build(self):
        app_root = MyW()
        return app_root


if __name__ == '__main__':
    MyApp().run()

