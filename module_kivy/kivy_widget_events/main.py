from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class MyW(Widget):
    def __init__(self, **kwargs):
        super(MyW, self).__init__(**kwargs)
        btn = Button(text='click me')
        btn.bind(on_press=self.on_press_callback, state=self.state_callback)
        self.add_widget(btn)

    def state_callback(self, obj, value):
        print(obj, value)

    def on_press_callback(self, obj):
        self.ids.label1.text = 'press on button'


class MyApp(App):
    def build(self):
        return MyW()


if __name__ == '__main__':
    MyApp().run()

