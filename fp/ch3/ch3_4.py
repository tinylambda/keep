if __name__ == '__main__':
    DIAL_CODE = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
    ]
    country_code = {
        country: code for code, country in DIAL_CODE
    }
    print(country_code)

    print({
        code: country.upper() for country, code in country_code.items() if code < 66
    })

