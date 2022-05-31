from somemodule import *


print(dir())
assert "blah" not in dir()
assert "spam" in dir()
assert "grok" in dir()
