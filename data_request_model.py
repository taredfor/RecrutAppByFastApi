from pydantic import BaseModel
from crud.auxiliary_class import Roles, Planets


class User(BaseModel):
    login: str
    first_name: str
    second_name: str
    planet: Planets
    e_mail: str
    pswd: str
    user_role: Roles

class Recrut(BaseModel):
    login: str
    first_name: str
    second_name: str
    planet: Planets
    e_mail: str
    pswd: str

class Question(BaseModel):
    question_id: int
    type_question: str
    content: str
    correct_answer: bool


class Answer(BaseModel):
    question_id: int
    user_answer: bool

class Login(BaseModel):
    user_login: str

class Email(BaseModel):
    e_mail: str




