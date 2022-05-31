from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.gesture import Gesture, GestureDatabase


gdb = GestureDatabase()

check = gdb.str_to_gesture(
    "eNq1l9tu3DYQhu/1It6bLjicE+cFtrcF/ACBYwv2Iqkt7G7a5u1DDqlT0lZ7I2Mxsj5JP2f4k"
    "xR1OH85//X9+Npfb98uffd7Ow6hO7wM0D0+vD/92T90Q8z/5gN218eH6+3y8aW/5lPqDl8H7g"
    "7/KvLot3WDFCnNzw8f5/dbeSyVx+w/Hvuj3NUNUDMoKXzPj0DsTuGIGiRJGCOVbP4pV7E7/Ra"
    "ORJZMwhS1u35++v9WyFvh7rU2ENEMJI1RuLu+NnEEgyhpjEG2xb1y0H3Ek4vbKA6kEmyKEWdx"
    "WPaJsaVN8eidH2Ef8ejiOIqHdbeQLvolaLTFLxlty7ulsVlaNBKChCnmEpp+uRSSIozRBLbl3"
    "dSoe8m7rdF2kkc3FmGSB1FVphYT6qSejY2sOsXtyYRuLOIkHgEtGrZIKJP4Spk13ZG524qzrX"
    "FWLlHmfok/9UvcFndTUe8Rz8OVA7RIYXtAoluKdke3hJU42j0dQ24pwV7ybiptm1oGE+Rz4il"
    "u9w25q8R3qQtnZ2WKd+TutpLeox4pZmt1jHlh3VR3X8nuUceFdIm4qc5uKy9mapCY339jXKb+"
    "08tjewlmN5VxH3H3lBcLcASZfzGv4osFPiVk5SnmCb6p766y7qbvvvL0Zg2GKtHGCDjPJ2FKi"
    "cfI2wuNuKsCu2i7qYLzdiP3BXGLYIs1DEAo0hh1eyaJeyq8i7b7KdM26ddNXpPO7SCSTnHbSn"
    "ErxXaQVndSJyeJGQOMMe+RJm1aLrk5bku7kYp7SLuPOvlI6/FHs4+87hH2Fats/p8vff8+beV"
    "Vyl5etTucMA/a7kSE+XAbNHVPmcGK2ZKBsxSciTPUyqAwUmdRKouFCToDqgwLU3MWQmVUmDnD"
    "1O7jwsCfOuXFt0JxGKNDaS1rhVwhV5gqpBW0CnEJLaw0G4QKwwrGmlJaQaxw1bp5QRBsBb2iZ"
    "MvczQtSWjGvx09m5uXwmnk1tNKDEGYbZli94TX0aqg1nRrE5Z3WoFdDtWyFBr0aqR2URljLqa"
    "1bbNDrsToywth69QfqGIrcaDVoPSoBqkNtbDE1Wi3iqsAtV6gesSdL0vKCalLNdqa5rjpB3vr"
    "z69utfJTmz8qTFclM/z6/3N4cSteSyvT28bW/PL0/935Ffdsd1n9Q7muT+dNw+Xj59lzFU+6W"
    "Y5L8ug5qwTR/PFH5bDz+AM/6Dqo="
)


def simple_gesture(name, point_list):
    g = Gesture()
    g.add_stroke(point_list)
    g.normalize()
    g.name = name
    return g


class GestureBoard(Widget):
    def __init__(self, *args, **kwargs):
        super(GestureBoard, self).__init__(*args, **kwargs)
        self.gdb = GestureDatabase()
        self.gdb.add_gesture(check)

    def on_touch_down(self, touch):
        useradata = touch.ud
        with self.canvas:
            Color(1, 1, 0)
            d = 30.0
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            useradata["line"] = Line(points=(touch.x, touch.y))
        return True

    def on_touch_move(self, touch):
        try:
            touch.ud["line"].points += [touch.x, touch.y]
            return True
        except KeyError as e:
            pass

    def on_touch_up(self, touch):
        g = simple_gesture(
            "", list(zip(touch.ud["line"].points[::2], touch.ud["line"].points[1::2]))
        )
        print("gesture representation: ", self.gdb.gesture_to_str(g))
        print("check: ", g.get_score(check))
        g2 = self.gdb.find(g, minscore=0.70)
        print(g2)
        if g2:
            if g2[1] == check:
                print("check")
        self.canvas.clear()


class MyApp(App):
    def build(self):
        return GestureBoard()


if __name__ == "__main__":
    MyApp().run()
