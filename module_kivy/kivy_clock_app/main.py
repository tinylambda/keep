from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex


LabelBase.register(
    name='Roboto',
    fn_regular='fonts/roboto/Roboto-Thin.ttf',
    fn_bold='fonts/roboto/Roboto-Medium.ttf',
)


class ClockApp(App):
    pass


if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#FF0080')
    ClockApp().run()

