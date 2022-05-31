from pydantic import BaseModel, validator


def normalize(name: str) -> str:
    return " ".join(word.capitalize() for word in name.split(" "))


class Producer(BaseModel):
    name: str

    _normalize_name = validator("name", allow_reuse=True)(normalize)


class Consumer(BaseModel):
    name: str

    _normalize_name = validator("name", allow_reuse=True)(normalize)


if __name__ == "__main__":
    jane_doe = Producer(name="JaNe DOE")
    john_doe = Consumer(name="joHN Doe")
    print(jane_doe)
    print(john_doe)
