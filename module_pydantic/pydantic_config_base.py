from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    v: str

    class Config:
        max_anystr_length = 10
        error_msg_templates = {
            "value_error.any_str.max_length": "max_length: {limit_value}",
        }
        thisismyconfig = 199


if __name__ == "__main__":
    try:
        Model(v="x" * 20)
    except ValidationError as e:
        print(e)

    m = Model(v="hi")
    print(m.Config.thisismyconfig)
