from urllib.parse import urljoin


print(urljoin(
    'http://www.example.com/path/',
    '/subpath/file.html'
))
print(urljoin(
    'http://www.example.com/path/',
    'subpath/file.html'
))

# if the path being joined to the URL starts with a /
# it resets the URL's path to the top level.

