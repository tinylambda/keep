import ssl
import urllib.request
import xml.etree.ElementTree as XML
from typing import Text, List, TextIO, Iterable, Tuple, TypeVar, Iterator

ssl._create_default_https_context = ssl._create_unverified_context


def row_iter_kml(file_obj: TextIO) -> Iterable[List]:
    ns_map = {
        'ns0': 'http://www.opengis.net/kml/2.2',
        'ns1': 'http://www.google.com/kml/ext/2.2',
        'ns2': 'http://earth.google.com/kml/2.1',
    }
    path_to_points = ('./ns2:Document/ns2:Placemark/'
                      'ns2:Point/ns2:coordinates')
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


T_ = TypeVar('T_')
Pairs_iter = Iterator[Tuple[T_, T_]]


def legs(lat_lon_iter: Iterator[T_]) -> Pairs_iter:
    begin = next(lat_lon_iter)
    for end in lat_lon_iter:
        yield begin, end
        begin = end


Text_Iter = Iterable[Tuple[Text, Text]]
LL_Iter = Iterator[Tuple[float, float]]


def float_from_pair(lat_lon_iter: Text_Iter) -> LL_Iter:
    return (
        (float(lat), float(lon))
        for lat, lon in lat_lon_iter
    )


url = 'https://raw.githubusercontent.com/googlearchive/kml-samples/gh-pages/kml_handbook/mvdoqq.kml'
with urllib.request.urlopen(url) as source:
    v1 = tuple(row_iter_kml(source))
print(v1)


with urllib.request.urlopen(url) as source:
    v2 = tuple(lat_lon_kml(row_iter_kml(source)))
print(v2)


with urllib.request.urlopen(url) as source:
    flt = ((float(lat), float(lon)) for lat, lon in lat_lon_kml(row_iter_kml(source)))
    for item in legs(flt):
        print(item)

print(tuple(flt))


with urllib.request.urlopen(url) as source:
    v3 = legs(float_from_pair(
        lat_lon_kml(
            row_iter_kml(source)
        )))
print(tuple(v3))


