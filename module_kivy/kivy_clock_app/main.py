from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

from time import strftime


class ClockApp(App):
    def update_time(self, nap):
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)


if __name__ == '__main__':
    LabelBase.register(
        name='Roboto',
        fn_regular='fonts/roboto/Roboto-Thin.ttf',
        fn_bold='fonts/roboto/Roboto-Medium.ttf',
    )
    Window.clearcolor = get_color_from_hex('#FF0080')
    ClockApp().run()

