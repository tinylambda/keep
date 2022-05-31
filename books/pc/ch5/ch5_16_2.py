import urllib.request
import io
import sys


u = urllib.request.urlopen("http://www.baidu.com/")
f = io.TextIOWrapper(u, encoding="utf-8")
text = f.read()

print(text)

print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="latin-1")
print(sys.stdout.encoding)
# sys.stdout.write('你好')  # error


f = open("sample.txt", "w")
print(f)
print(f.buffer)
print(f.buffer.raw)

print("-" * 100)

f = io.TextIOWrapper(f.buffer, encoding="latin-1")
print(f)
# f.write('Hello')  # ValueError: I/O operation on closed file.

f = open("sample.txt", "w")
print(f)

b = f.detach()
print(b)

# f.write('hello')  # ValueError: underlying buffer has been detached

f = io.TextIOWrapper(b, encoding="latin-1")
print(f)

sys.stdout = io.TextIOWrapper(
    sys.stdout.detach(), encoding="ascii", errors="xmlcharrefreplace"
)
print("Jalape\u00f1o")
