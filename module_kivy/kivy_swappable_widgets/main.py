from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen


letters = ['txt 1', 'txt 2', 'txt 3', 'txt 4', 'txt 5', 'txt 6']


class MButton(Button):
    pass


class MyW(BoxLayout):
    def __init__(self, **kwargs):
        super(MyW, self).__init__(**kwargs)
        for l in letters:
            s = Screen(name=l)
            s.add_widget(Label(text=l))
            self.ids.sm.add_widget(s)
            self.ids.buttons.add_widget(MButton(text=l))


class MyApp(App):
    def build(self):
        return MyW()


if __name__ == '__main__':
    MyApp().run()


