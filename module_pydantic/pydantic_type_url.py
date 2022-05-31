from typing import Optional

from pydantic import BaseModel, HttpUrl, ValidationError, PostgresDsn


class MyModel(BaseModel):
    url: HttpUrl
    db: Optional[PostgresDsn]


if __name__ == "__main__":
    m = MyModel(url="https://www.baidu.com")
    print(m.url)
    print(m.url.scheme)
    print(m.url.host)
    print(m.url.port)
    print(m.url.host_type)

    try:
        MyModel(url="ftp://badone")
    except ValidationError as e:
        print(e)

    try:
        MyModel(url="not a url")
    except ValidationError as e:
        print(e)

    m = MyModel(
        url="https://www.baidu.com", db="postgres://user:pass@localhost:5632/foobar"
    )
    print(m.db)
    m = MyModel(url="https://www.baidu.com", db="postgres://user:pass@localhost:5632")
    print(m)
