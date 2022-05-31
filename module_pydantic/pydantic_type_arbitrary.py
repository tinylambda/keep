from pydantic import BaseModel, ValidationError


class Pet:
    def __init__(self, name: str):
        self.name = name


class Model(BaseModel):
    pet: Pet
    owner: str

    class Config:
        arbitrary_types_allowed = True


if __name__ == "__main__":
    pet = Pet(name="Hedwig")
    m = Model(owner="Felix", pet=pet)
    print(m)
    print(m.pet)
    print(m.pet.name)
    print(type(m.pet))

    try:
        Model(owner="Felix", pet="Hewig")
    except ValidationError as e:
        print(e)

    # Nothing in the instance of the arbitrary type is checked
    # Here name probably should have been a str, but it's not validated
    pet2 = Pet(name=42)
    m2 = Model(owner="Felix", pet=pet2)
    print(m2)
    print(m2.pet)
    print(m2.pet.name)
    print(type(m2.pet))
