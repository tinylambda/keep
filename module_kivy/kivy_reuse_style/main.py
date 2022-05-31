from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class MyWidget1(BoxLayout):
    writing = StringProperty("XYZ")

    def text(self, val):
        print("text input text is : {txt}".format(txt=val))


class MyWidget2(BoxLayout):
    writing = StringProperty()

    def text(self, val):
        self.writing = val


class MyW(BoxLayout):
    def __init__(self, **kwargs):
        super(MyW, self).__init__(**kwargs)
        self.add_widget(MyWidget1())
        self.add_widget(MyWidget2())


class MyApp(App):
    def build(self):
        return MyW()


if __name__ == "__main__":
    MyApp().run()
