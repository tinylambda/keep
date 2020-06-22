from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_location(self):
        print('The user searched for "{}"'.format(self.search_input.text))
        appid = '54f64871388416c8ff4a4b198787e8b1'
        search_template = 'http://api.openweathermap.org/data/2.5/find?q={}&type=like&appid={}'
        search_url = search_template.format(self.search_input.text, appid)
        print(search_url)
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):
        cities = ['{} ({})'.format(d['name'], d['sys']['country']) for d in data['list']]
        print('\n'.join(cities))


class WeatherApp(App):
    pass


if __name__ == '__main__':
    WeatherApp().run()

