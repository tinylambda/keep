from urllib.parse import urlparse, urlunparse


original = "http://netloc/path;?#"
print("ORIG: ", original)
parsed = urlparse(original)
print("PARSED: ", type(parsed), parsed)
t = parsed[:]
print("TUPLE: ", type(t), t)
print("NEW: ", urlunparse(t))
