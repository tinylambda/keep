from unittest.mock import patch

x = 87

with patch("__main__.x"):
    print(x)

print(x)


with patch("__main__.x", "patched_value"):
    print(x)

print(x)
