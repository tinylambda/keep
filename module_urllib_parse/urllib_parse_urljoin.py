from urllib.parse import urljoin


print(urljoin(
    'http://www.example.com/path/file.html',
    'anotherfile.html'
))
print(urljoin(
    'http://www.example.com/path/file.html',
    '../anotherfile.html'
))

#  non-relative paths are handled in the same way as by os.path.join()

