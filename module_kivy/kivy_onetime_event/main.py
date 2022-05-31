from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock


class MyW(Widget):
    def my_callback(self, dt):
        self.ids.label1.text = "My callback is called @!" + str(dt)

    def on_touch_down(self, touch):
        # Here schedule a one-time event
        Clock.schedule_once(self.my_callback, 2)


class MyApp(App):
    def build(self):
        return MyW()


if __name__ == "__main__":
    MyApp().run()
