import urllib.parse

from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, ListProperty, NumericProperty
from kivy.storage.jsonstore import JsonStore
from kivy.clock import Clock

WEATHER_APP_ID = '54f64871388416c8ff4a4b198787e8b1'


class WeatherRoot(BoxLayout):
    add_location_form_widget = ObjectProperty()
    carousel_widget = ObjectProperty()
    locations_widget = ObjectProperty()
    current_weather_widget = ObjectProperty()
    forecast_widget = ObjectProperty()

    def __init__(self, **kwargs):
        super(WeatherRoot, self).__init__(**kwargs)

        self.json_store = JsonStore('weather_store.json')
        if self.json_store.exists('locations'):
            locations = self.json_store.get('locations')
            self.locations_widget.locations_list.data.extend(locations['locations'])
            current_location = locations['current_location']
            self.show_current_weather(current_location)
        else:
            Clock.schedule_once(lambda dt: self.show_add_location_form_widget())

    def show_add_location_form_widget(self):
        self.add_location_form_widget = AddLocationForm()
        self.add_location_form_widget.open()

    def show_current_weather(self, location=None):
        exists_origin_locations = [item['origin'] for item in self.locations_widget.locations_list.data]
        if location not in exists_origin_locations:
            self.locations_widget.locations_list.data.append({'origin': location})
            self.json_store.put('locations',
                                locations=list(self.locations_widget.locations_list.data),
                                current_location=location
                                )
        self.current_weather_widget.location = location
        self.forecast_widget.location = location

        self.current_weather_widget.update_weather()
        self.forecast_widget.update_weather()

        if self.add_location_form_widget is not None:
            self.add_location_form_widget.dismiss()
        self.carousel_widget.load_slide(self.current_weather_widget)


class Locations(BoxLayout):
    locations_list = ObjectProperty()


class CurrentWeather(BoxLayout):
    # Will show the weather of the location below (can use GPS to retrieve the default value)
    location = ListProperty(['Beijing', 'CN'])
    # Will use the data from weather API to fulfill the following properties
    conditions = StringProperty()
    temp = NumericProperty()
    temp_min = NumericProperty()
    temp_max = NumericProperty()

    def __init__(self, **kwargs):
        super(CurrentWeather, self).__init__(**kwargs)

    def update_weather(self):
        config = WeatherApp.get_running_app().config
        temp_type = config.getdefault('General', 'temp_type', 'metric').lower()
        weather_template = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&units={}&appid={}'
        weather_url = weather_template.format(
            urllib.parse.quote(self.location[0]),
            urllib.parse.quote(self.location[1]),
            temp_type, WEATHER_APP_ID
        )
        request = UrlRequest(weather_url, self.weather_retrieved)

    def weather_retrieved(self, request, data):
        self.conditions = data['weather'][0]['description']
        self.temp = data['main']['temp']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']


class Forecast(BoxLayout):
    location = ListProperty()

    def update_weather(self):
        pass

    def weather_retrieved(self, request, data):
        pass


class AddLocationForm(ModalView):
    search_input = ObjectProperty()
    search_results = ObjectProperty()

    def search_location(self):
        search_template = 'http://api.openweathermap.org/data/2.5/find?q={}&type=like&appid={}'
        search_url = search_template.format(
            urllib.parse.quote(self.search_input.text),
            WEATHER_APP_ID
        )
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):
        cities = [{'origin': (d['name'], d['sys']['country'])} for d in data['list']]
        self.search_results.data.clear()
        self.search_results.data.extend(cities)


class SelectableLabel(RecycleDataViewBehavior, Button):
    """ Add selection support to the Label """
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    location = ListProperty()

    def refresh_view_attrs(self, rv, index, data):
        """ Catch and handle the view changes """
        self.index = index
        data_origin = data.get('origin', ('None', 'None'))
        self.location = data_origin
        data.update({'text': f'{data_origin[0]} ({data_origin[1]})'})
        return super(SelectableLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        """ Add selection on touch down """
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        """ Respond to the selection of items in the view. """
        self.selected = is_selected


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    """ Adds selection and focus behaviour to the view. """


class WeatherApp(App):
    def build(self):
        weather_root = WeatherRoot()
        return weather_root

    def on_pause(self):
        print('On Pasuse....................................')


if __name__ == '__main__':
    WeatherApp().run()

