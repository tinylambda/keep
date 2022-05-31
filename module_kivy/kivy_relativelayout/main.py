from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout


class MyW1(RelativeLayout):
    def __init__(self, **kwargs):
        super(MyW1, self).__init__(**kwargs)
        self.size = (300, 300)
        self.pos = (300, 0)


class MyW(FloatLayout):
    def __init__(self, **kwargs):
        super(MyW, self).__init__(**kwargs)
        self.myw1_name = MyW1()
        self.add_widget(self.myw1_name)


class MyApp(App):
    def build(self):
        app_root = MyW()
        print(app_root.size)
        return app_root


if __name__ == "__main__":
    MyApp().run()
