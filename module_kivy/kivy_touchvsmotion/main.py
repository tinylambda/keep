from kivy.app import App
from kivy.uix.widget import Widget


# We also know that a touch event always has the pos profile
# , namely position information. The motion event, however,
# is not dispatched throughout the widget tree.
class MyW(Widget):
    def on_touch_move(self, touch):
        if "pos" in touch.profile:
            self.ids.button1.pos = touch.pos

    def on_touch_down(self, touch):
        if "button" in touch.profile:
            self.ids.button1.text = touch.button


class MyApp(App):
    def build(self):
        return MyW()


if __name__ == "__main__":
    MyApp().run()
