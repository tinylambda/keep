import geoip2.database

if __name__ == "__main__":
    with geoip2.database.Reader(
        "/Users/Felix/Downloads/GeoLite2-City_20220816/GeoLite2-City.mmdb"
    ) as reader:
        response = reader.city("98.42.103.101")
        print(response.country, response.city)
