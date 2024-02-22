from uuid import UUID
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    admin: bool = False
    depositBearer: bool = False
    rentalChecker: bool = False
    appointmentManager: bool = False
    treasurer: bool = False


class UserCreate(UserBase):
    password_cleartext: str
    pin_cleartext: str | None = None
    pass


class User(UserBase):
    id: UUID
    softDeleted: bool

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    passwordCleartext: str | None = None
    pinCleartext: str | None = None
    admin: bool | None = None
    depositBearer: bool | None = None
    rentalChecker: bool | None = None
    appointmentManager: bool | None = None
    treasurer: bool | None = None
    softDeleted: bool | None = None
