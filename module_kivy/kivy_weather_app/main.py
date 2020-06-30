from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.properties import ObjectProperty, BooleanProperty, ListProperty, StringProperty, NumericProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.factory import Factory

WEATHER_APP_ID = '54f64871388416c8ff4a4b198787e8b1'


class WeatherRoot(BoxLayout):
    current_weather = ObjectProperty()

    def show_current_weather(self, location=None):
        self.clear_widgets()

        if location is None and self.current_weather is None:
            location = ('New York', 'US')

        if location is not None:
            self.current_weather = CurrentWeather(location=location)

        self.current_weather.update_weather()
        self.add_widget(self.current_weather)

    def show_add_location_form(self):
        self.clear_widgets()
        self.add_widget(AddLocationForm())


class Conditions(BoxLayout):
    conditions = StringProperty()


class CurrentWeather(BoxLayout):
    location = ListProperty(['New York', 'US'])
    conditions = ObjectProperty()
    temp = NumericProperty()
    temp_min = NumericProperty()
    temp_max = NumericProperty()

    def update_weather(self):
        weather_template = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid={}'
        weather_url = weather_template.format(*self.location, WEATHER_APP_ID)
        request = UrlRequest(weather_url, self.weather_retrieved)

    def weather_retrieved(self, request, data):
        self.render_conditions(data['weather'][0]['description'])
        self.temp = data['main']['temp']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']

    def render_conditions(self, conditions_description):
        if 'clear' in conditions_description.lower():
            conditions_widget = Factory.ClearConditions()
        else:
            conditions_widget = Factory.UnknownConditions()
        conditions_widget.conditions = conditions_description
        self.conditions.clear_widgets()
        self.conditions.add_widget(conditions_widget)


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()

    def search_location(self):
        print('The user searched for "{}"'.format(self.search_input.text))
        search_template = 'http://api.openweathermap.org/data/2.5/find?q={}&type=like&appid={}'
        search_url = search_template.format(self.search_input.text, WEATHER_APP_ID)
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):
        cities = [{'origin': (d['name'], d['sys']['country'])} for d in data['list']]
        self.search_results.data.clear()
        self.search_results.data.extend(cities)
        print(f"self.search_results.data={self.search_results.data}")


class SelectableLabel(RecycleDataViewBehavior, Button, Label):
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
        print('apply selection...')
        self.selected = is_selected


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    """ Adds selection and focus behaviour to the view. """
    

class WeatherApp(App):
    pass


if __name__ == '__main__':
    WeatherApp().run()

