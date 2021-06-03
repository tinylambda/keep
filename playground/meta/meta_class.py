from example.package.meta_example import BlueprintMeta


class Blueprint(metaclass=BlueprintMeta):
    pass


class Build(Blueprint):
    name = "hello"


class FarmBuild(Build):
    age = 1001


if __name__ == '__main__':
    pass

