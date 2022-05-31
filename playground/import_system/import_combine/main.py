import sys
import importlib

sys.path.extend(["foo-package", "bar-package"])

import spam.blah
import spam.grok

import spam

print(spam.__path__)
print(spam)

importlib.reload(spam)


sys.path.append("mypackage")
import spam.custom

spam.custom.test_func()
