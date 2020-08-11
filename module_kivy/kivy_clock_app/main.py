from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from time import strftime


class ClockApp(App):
    sw_seconds = 0
    sw_started = False

    def update_time(self, nap):
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

    def update_stop_watch(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
        minutes, seconds = divmod(self.sw_seconds, 60)
        self.root.ids.stopwatch_label.text = '%02d:%02d.[size=40]%02d[/size]' % \
                                       (int(minutes), int(seconds), int(seconds * 100 % 100))

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)
        Clock.schedule_interval(self.update_stop_watch, 0.016)

    def start_stop(self):
        self.sw_started = not self.sw_started
        print(self.root.ids)
        self.root.ids.stopwatch.text = 'Stop' if self.sw_started else 'Start'

    def reset(self):
        if self.sw_started:
            self.root.ids.stopwatch.text = 'Start'
            self.sw_started = False
        self.sw_seconds = 0


if __name__ == '__main__':
    LabelBase.register(
        name='Roboto',
        fn_regular='fonts/roboto/Roboto-Thin.ttf',
        fn_bold='fonts/roboto/Roboto-Medium.ttf',
    )
    Window.clearcolor = get_color_from_hex('#FF0080')
    ClockApp().run()

