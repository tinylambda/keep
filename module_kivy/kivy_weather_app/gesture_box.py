from kivy.uix.boxlayout import BoxLayout


class GestureBox(BoxLayout):
    def on_touch_down(self, touch):
        touch.ud["gesture_path"] = [(touch.x, touch.y)]  # ud is short for user data
        super(GestureBox, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        touch.ud["gesture_path"].append((touch.x, touch.y))
        super(GestureBox, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        print(touch.ud["gesture_path"])
        super(GestureBox, self).on_touch_up(touch)
