from unittest.mock import MagicMock

m = MagicMock(return_value=10)
print(m(1, 2, debug=True))
m.assert_called_with(1, 2, debug=True)
# m.assert_called_with(1, 2)  # AssertionError
m.upper.return_value = "HELLO"
m.upper("hello")
assert m.upper.called
m.upper.assert_called()

m.split.return_value = ["hello", "world"]
m.split("hello world")
m.split.assert_called_with("hello world")

print(m["blah"])
print(m.__getitem__.called)
m.__getitem__.assert_called_with("blah")
