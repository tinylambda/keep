from pydantic import BaseModel, SecretStr, SecretBytes, ValidationError


class SimpleModel(BaseModel):
    password: SecretStr
    password_bytes: SecretBytes


class SimpleModelDumpable(BaseModel):
    password: SecretStr
    password_bytes: SecretBytes

    class Config:
        json_encoders = {
            SecretStr: lambda v: v.get_secret_value() if v else None,
            SecretBytes: lambda v: v.get_secret_value() if v else None,
        }


if __name__ == "__main__":
    sm = SimpleModel(password="Password", password_bytes=b"passwordbytes")
    print(sm)
    print(sm.password)
    print(sm.password_bytes)
    print(sm.dict())
    print(sm.json())

    try:
        SimpleModel(password=[1, 2, 3], password_bytes=[1, 2, 3])
    except ValidationError as e:
        print(e)

    sm2 = SimpleModelDumpable(password="Password", password_bytes=b"passwordbytes")
    print(sm2)
    print(sm2.password)
    print(sm2.password_bytes)
    print(sm2.dict())
    print(sm2.json())
