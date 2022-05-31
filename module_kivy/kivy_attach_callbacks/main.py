from kivy.app import App
from kivy.uix.widget import Widget


def my_callback(value, *args):
    print("Hello , I got an event!", args)


class MyW(Widget):
    def __init__(self, **kwargs):
        super(MyW, self).__init__(**kwargs)
        self.register_event_type("on_swipe")

    def on_swipe(self, value):
        self.ids.label1.text = "Hello1"

    def do_something(self, value):
        if self.ids.button1.text != "Hello":
            self.dispatch("on_swipe", value)

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            self.ids.button1.text = "xxx"
        if touch.is_triple_tap:
            self.ids.button1.text = "Hello"
        self.bind(on_swipe=my_callback)
        self.do_something("test")


class MyApp(App):
    def build(self):
        return MyW()


if __name__ == "__main__":
    MyApp().run()
