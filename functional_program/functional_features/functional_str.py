from decimal import *
from typing import Text, Optional


def clean_decimal(text: Text) -> Optional[Text]:
    if text is None:
        return None
    return Decimal(
        text.replace('$', '').replace(',', '')
    )


def replace(s: Text, a: Text, b: Text):
    return s.replace(a, b)


def clean_decimal_v2(text: Text) -> Optional[Text]:
    if text is None:
        return None
    return Decimal(
        replace(replace(text, '$', ''), ',', '')
    )


def remove(s: Text, chars: Text) -> Text:
    if chars:
        return remove(
            s.replace(chars[0], ''),
            chars[1:]
        )
    return s


def clean_decimal_v3(text: Text) -> Optional[Text]:
    if text is None:
        return None
    return Decimal(remove(text, '$,'))


if __name__ == '__main__':
    s_: Text = '$100,000.1'
    print(clean_decimal(s_))
    print(clean_decimal_v2(s_))
    print(clean_decimal_v3(s_))

