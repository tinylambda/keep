from kivy.app import App
from kivy.core.text import LabelBase

LabelBase.register(
    name='Roboto',
    fn_regular='fonts/roboto/Roboto-Thin.ttf',
    fn_bold='fonts/roboto/Roboto-Medium.ttf',
)


class ClockApp(App):
    pass


if __name__ == '__main__':
    ClockApp().run()

