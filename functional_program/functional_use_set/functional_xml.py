import ssl
import urllib.request
import xml.etree.ElementTree as XML
from typing import Text, List, TextIO, Iterable, Tuple

ssl._create_default_https_context = ssl._create_unverified_context


def row_iter_kml(file_obj: TextIO) -> Iterable[List]:
    ns_map = {
        'ns0': 'http://www.opengis.net/kml/2.2',
        'ns1': 'http://www.google.com/kml/ext/2.2'
    }
    path_to_points = ('./ns0:Document/ns0:Placemark/'
                      'ns0:Point/ns0:coordinates')
    doc = XML.parse(file_obj)
    return (comma_split(Text(coordinates.text))
            for coordinates in
            doc.findall(path_to_points, ns_map))


def comma_split(text: Text) -> List[Text]:
    return text.split(',')


def pick_lat_lon(lon: Text, lat: Text, alt: Text) -> Tuple[Text, Text]:
    return lat, lon


Rows = Iterable[List[Text]]
LL_Text = Tuple[Text, Text]


def lat_lon_kml(row_iter: Rows) -> Iterable[LL_Text]:
    return (pick_lat_lon(*row) for row in row_iter)


url = 'https://raw.githubusercontent.com/googlearchive/kml-samples/gh-pages/kml/Placemark/Point/altitude.kml'
with urllib.request.urlopen(url) as source:
    v1 = tuple(row_iter_kml(source))
print(v1)


with urllib.request.urlopen(url) as source:
    v2 = tuple(lat_lon_kml(row_iter_kml(source)))
print(v2)

