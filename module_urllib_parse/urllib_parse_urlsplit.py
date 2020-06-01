from urllib.parse import urlsplit


url = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'
parsed = urlsplit(url)

print('scheme: ', parsed.scheme)
print('netloc: ', parsed.netloc)
print('path: ', parsed.path)
print('query: ', parsed.query)
print('fragment: ', parsed.fragment)
print('username: ', parsed.username)
print('password: ', parsed.password)
print('port: ', parsed.port)

