from data.dto.base import BaseDTO
from pydantic import EmailStr, validator
from data.dao.account import AccountEntity
from typing import Optional


class BaseAccountDTO(BaseDTO):

    username: str
    role: str
    email: EmailStr
    firstname: Optional[str]
    lastname: Optional[str]

    @validator('role')
    def validate_role(cls, role):
        if role in ["admin", "user"]:
            return role
        else:
            raise ValueError(
                f"Wrong role: {role}. Should be admin or user")


class ReadAccountDTO(BaseAccountDTO):

    id: int

    @classmethod
    def from_entity(cls, entity: AccountEntity):
        return ReadAccountDTO(id=entity.id,
                              username=entity.username,
                              role=entity.role,
                              email=entity.email,
                              firstname=entity.firstname,
                              lastname=entity.lastname)


class CreateAccountDTO(BaseAccountDTO):

    password: str


class UpdateAccountDTO(CreateAccountDTO):
    pass
