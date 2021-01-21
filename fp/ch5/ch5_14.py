from collections import namedtuple
from operator import attrgetter


if __name__ == '__main__':
    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ]

    LatLong = namedtuple('LatLong', 'lat long')
    Metropolis = namedtuple('Metropolis', 'name cc pop coord')

    metro_ares = [
        Metropolis(name, cc, pop, LatLong(lat, long))
        for name, cc, pop, (lat, long) in metro_data
    ]

    print(metro_ares[0])

    name_lat = attrgetter('name', 'coord.lat')

    for city in sorted(metro_ares, key=attrgetter('coord.lat')):
        print(name_lat(city))

