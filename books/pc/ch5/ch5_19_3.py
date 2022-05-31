import tempfile


result = tempfile.mkstemp()
print(result)

result = tempfile.mkdtemp()
print(result)

result = tempfile.gettempdir()
print(result)

f = tempfile.NamedTemporaryFile(prefix="mytemp", suffix=".txt", dir="/tmp")
print(f.name)
