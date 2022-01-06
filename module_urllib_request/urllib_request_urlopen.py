from urllib import request


if __name__ == '__main__':
    response = request.urlopen('http://localhost:8080')
    print('RESPONSE: ', response)
    print('URL: ', response.geturl())

    headers = response.info()
    print('DATE: ', headers['date'])
    print('HEADERS: ')
    print('--------')
    print(headers)

    data = response.read().decode('utf-8')
    print('LENGTH: ', len(data))
    print('DATA: ')
    print('--------')
    print(data)
