import re


if __name__ == "__main__":
    text = "UPPER PYTHON, lower python, Mixed Python"
    result = re.findall("python", text, flags=re.IGNORECASE)
    print(result)

    result = re.sub("python", "snake", text, flags=re.IGNORECASE)
    print(result)

    def matchcase(word):
        def replace(m):
            text = m.group()
            if text.isupper():
                return word.upper()
            elif text.islower():
                return word.lower()
            elif text[0].isupper():
                return word.capitalize()
            else:
                return word

        return replace

    result = re.sub("python", matchcase("snake"), text, flags=re.IGNORECASE)
    print(result)
