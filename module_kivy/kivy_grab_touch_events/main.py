from kivy.app import App
from kivy.uix.widget import Widget


class MyW(Widget):
    def on_touch_down(self, touch):
        if self.ids.button1.collide_point(*touch.pos):
            touch.grab(self)
            return True

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            self.ids.label1.text = "Click on the screen but over the Button"
            touch.ungrab(self)
            return True
        else:
            self.ids.label1.text = "Click on the screen"


class MyApp(App):
    def build(self):
        return MyW()


if __name__ == "__main__":
    MyApp().run()
