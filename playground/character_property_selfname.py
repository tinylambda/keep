class A:
    CONCEPT_NAME = "character"

    def __init__(self):
        self._level: int = 1

    @property
    def level(self):
        my_name = f"{self.CONCEPT_NAME}.level"
        print(f"getting {my_name}")
        return self._level

    @level.setter
    def level(self, value):
        my_name = f"{self.CONCEPT_NAME}.level"
        game_context = {}
        max_level = game_context.get("max_level", 10)
        if value > max_level:
            raise RuntimeError(f"Max level {max_level} !")
        print(f"setting {my_name} to value {value}")
        self._level = value


if __name__ == "__main__":
    a = A()
    print(a.level)
    a.level = 8
    print(a.level)

    a.level += 1
    print(a.level)

    a.level += 1
    print(a.level)

    try:
        a.level += 1
        print(a.level)
    except RuntimeError:
        print("Error occurred")

    print(a.level)
