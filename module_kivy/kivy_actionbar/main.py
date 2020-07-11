from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class MyW(FloatLayout):
    def __init__(self, **kwargs):
        super(MyW, self).__init__(**kwargs)
        self.add_widget(MyW1())


class MyW1(FloatLayout):
    pass


class MyApp(App):
    def build(self):
        return MyW()


if __name__ == '__main__':
    MyApp().run()

