from urllib.parse import urlparse


url = "http://netloc/path;param?query=arg#frag"
parsed = urlparse(url)
print(parsed)
