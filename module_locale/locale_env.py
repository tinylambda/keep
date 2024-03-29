import locale
import os
import pprint

locale.setlocale(locale.LC_ALL, "")

print("Environment settings:")
for env_name in ["LC_ALL", "LC_CTYPE", "LANG", "LANGUAGE"]:
    print("{} = {}".format(env_name, os.environ.get(env_name, "")))


# What is the locale
print("\nLocale from environment: ", locale.getlocale())
template = """
Numeric formatting:
Decimal point: "{decimal_point}"
Grouping positions: {grouping}
Thousands separator: {thousands_sep}

Monetary formatting:
International currency symbol: "{int_curr_symbol!r}"
Local currency symbol:  {currency_symbol!r}
Symbol precedes positive value: {p_cs_precedes}
Symbol precedes negative value: {n_cs_precedes}
Decimal point: "{frac_digits}"
international: {int_frac_digits}
Grouping positions: {mon_grouping}
Thousands separator: "{mon_thousands_sep}"
Positive sign: {positive_sign}
Positive sign position: {p_sign_posn}
Negative sign: {negative_sign}
Negative sign position: {n_sign_posn}
"""

sign_positions = {
    0: "Surrounded by parentheses",
    1: "Before value and symbol",
    2: "After value and symbol",
    3: "Before value",
    4: "After value",
    locale.CHAR_MAX: "Unspecified",
}

info = {}
info.update(locale.localeconv())
info["p_sign_posn"] = sign_positions[info["p_sign_posn"]]
info["n_sign_posn"] = sign_positions[info["n_sign_posn"]]

print(template.format(**info))


# LANG=zh_CN LC_CTYPE=cn python module_locale/locale_env.py
