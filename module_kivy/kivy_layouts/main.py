from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout


class MyW(Widget):
    def __init__(self, **kwargs):
        super(MyW, self).__init__(**kwargs)
        self.my_w1 = MyW1()
        self.add_widget(self.my_w1)


class MyW1(FloatLayout):
    def __init__(self, **kwargs):
        super(MyW1, self).__init__(**kwargs)
        self.size = (300, 300)


class MyApp(App):
    def build(self):
        app_root = MyW()
        return app_root


if __name__ == '__main__':
    MyApp().run()

