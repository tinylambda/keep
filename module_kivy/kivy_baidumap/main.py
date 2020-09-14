from kivy.app import App
from kivy.uix.widget import Widget
from kivy_garden.mapview import MapView


class MapApp(App):
    def build(self):
        return MapView(zoom=11, lat=50.6394, lon=3.057)


if __name__ == '__main__':
    MapApp().run()

