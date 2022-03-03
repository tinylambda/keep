from pydantic import BaseModel


def to_camel(string: str) -> str:
    return ''.join(word.capitalize() for word in string.split('_'))


class Voice(BaseModel):
    name: str
    language_code: str

    class Config:
        alias_generator = to_camel


if __name__ == '__main__':
    voice = Voice(Name='Filiz', LanguageCode='zh-CN')
    print(voice.language_code)
    print(voice.dict())
    print(voice.dict(by_alias=True))
