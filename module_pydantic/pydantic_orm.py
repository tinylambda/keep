from typing import List, Dict

from pydantic import BaseModel, constr, Field
from sqlalchemy import Column, Integer, String, ARRAY, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CompanyOrm(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)
    domains = Column(ARRAY(String(255)))


class CompanyModel(BaseModel):
    id: int
    public_key: constr(max_length=20)
    domains: List[constr(max_length=255)]

    class Config:
        orm_mode = True


co_orm = CompanyOrm(
    id=123, public_key="foobar", name="Testing", domains=["example.com", "foobar.com"]
)
print(co_orm)

co_model = CompanyModel.from_orm(co_orm)
print(co_model)


class MyModel(BaseModel):
    metadata: Dict[str, str] = Field(alias="metadata_")

    class Config:
        orm_mode = True


class SqlModel(Base):
    __tablename__ = "my_table"

    id = Column("id", Integer, primary_key=True)
    # metadata is reserved by SQLAlchemy, hence the '_'
    metadata_ = Column("metadata", JSON)


sql_model = SqlModel(metadata_={"key": "val"}, id=1)
pydantic_model = MyModel.from_orm(sql_model)
print(pydantic_model.dict())
print(pydantic_model.dict(by_alias=True))
