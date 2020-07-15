from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.properties import AliasProperty
import random


def get_right(self):
    return self.x + self.width


def set_right(self, value):
    self.x = value - self.width


right = AliasProperty(
        getter=get_right,
        setter=set_right,
        bind=('x', 'width')
    )


def on_right():
    print('Hello')


class RootWidget(Widget):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text='btn 1', pos=(0, 100)))
        self.add_widget(Button(text='btn 2', pos=(100, 0)))

        cb = CustomBtn()
        cb.bind(pressed=self.btn_pressed, right=self.btn_right)
        self.add_widget(cb)

    def btn_pressed(self, instance, pos):
        print('pos: printed from root widget: {pos}'.format(pos=pos))

    def btn_right(self, instance, val):
        print('VAL: ', val)


class CustomBtn(Widget):
    pressed = ListProperty([0, 0])
    right = AliasProperty(
        getter=get_right,
        setter=set_right,
        bind=('x', 'width')
    )

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            if random.random() > 0.5:
                print('x...')
                self.x += 1
            else:
                print('width...')
                self.width += 1
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        print('pressed at {pos}'.format(pos=pos))

    # def on_right(self, instance, value):
    #     print('on_right..')


class MyApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MyApp().run()

