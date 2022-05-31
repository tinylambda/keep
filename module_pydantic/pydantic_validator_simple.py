from pydantic import BaseModel, validator, ValidationError


class UserModel(BaseModel):
    name: str
    username: str
    password1: str
    password2: str

    @validator("name")
    def name_must_contain_space(cls, v):
        if " " not in v:
            raise ValueError("must contain a space")
        return v.title()

    @validator("password2")
    def passwords_match(cls, v, values, **kwargs):
        if "password1" in values and v != values["password1"]:
            raise ValueError("passwords do not match")
        return v

    @validator("username")
    def username_alphanumeric(cls, v):
        assert v.isalnum(), "must be alphanumeric"
        return v


if __name__ == "__main__":
    user = UserModel(
        name="Felix Pan",
        username="tinylambda",
        password1="abc123",
        password2="abc123",
    )
    print(user)

    try:
        UserModel(
            name="felix",
            username="felix",
            password1="abc123",
            password2="abc456",
        )
    except ValidationError as e:
        print(e)
