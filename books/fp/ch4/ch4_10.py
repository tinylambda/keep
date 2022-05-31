from unicodedata import normalize, name


if __name__ == "__main__":
    ohm = "\u2126"
    print(name(ohm))

    ohm_c = normalize("NFC", ohm)
    print(name(ohm_c))

    print(ohm, ohm_c, ohm == ohm_c)

    print(normalize("NFC", ohm) == normalize("NFC", ohm_c))
