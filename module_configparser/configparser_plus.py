from configparser import ConfigParser


class ConfigWriterWithRepeatKeys(ConfigParser):
    _DEFAULT_INTERPOLATION = None  # Disable interpolation

    def __init__(self, *args, **kwargs):
        super().__init__(*args, strict=True, **kwargs)

    def _validate_value_types(self, *, section="", option="", value=""):
        """
        Add support for list.
        """
        if not isinstance(section, str):
            raise TypeError("section names must be strings")
        if not isinstance(option, str):
            raise TypeError("option keys must be strings")
        if not self._allow_no_value or value:
            if not isinstance(value, (str, list)):
                raise TypeError("option values must be strings or list of strings")

    def _write_section(self, fp, section_name, section_items, delimiter):
        """Write a single section to the specified `fp'."""
        fp.write("[{}]\n".format(section_name))
        for key, value in section_items:
            value = self._interpolation.before_write(self, section_name, key, value)
            if value is not None or not self._allow_no_value:
                if isinstance(value, str):
                    value = delimiter + str(value).replace("\n", "\n\t")
                    fp.write("{}{}\n".format(key, value))
                elif isinstance(value, list):
                    for _value in value:
                        _value = delimiter + str(_value).replace("\n", "\n\t")
                        fp.write("{}{}\n".format(key, _value))
            else:
                value = ""
                fp.write("{}{}\n".format(key, value))
        fp.write("\n")


if __name__ == "__main__":
    cpp = ConfigWriterWithRepeatKeys()
    test_section_name = "test_section"
    cpp.add_section(test_section_name)
    cpp.set(test_section_name, "http", "0.0.0.0:8000")
    cpp.set(
        test_section_name,
        "http-to",
        [
            "192.168.173.1:3031",
            "192.168.173.2:3031",
            "192.168.173.3:3031",
            "192.168.173.4:3031",
        ],
    )
    cpp.add_section("test2")
    cpp.add_section("test3")
    cpp.set("test3", "http", "0.0.0.0:80")

    with open("/tmp/test.ini", "w") as f:
        cpp.write(f, space_around_delimiters=True)
