from pydantic import BaseModel


class BaseDTO(BaseModel):

    class Config:
        validate_assignment = True
