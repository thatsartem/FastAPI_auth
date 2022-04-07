from uuid import UUID
from pydantic import BaseModel


class UserIn(BaseModel):
    username: str
    password: str


class User(BaseModel):
    id: int
    username: str
    key: UUID

    class Config:
        orm_mode = True
