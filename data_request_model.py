from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    second_name: str
    planet: str
    e_mail: str
