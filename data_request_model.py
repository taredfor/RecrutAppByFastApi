from pydantic import BaseModel
from enum import Enum


class User(BaseModel):
    class Roles(Enum):
        USER = "USER"
        RECRUT = "RECRUT"
        ADMIN = "ADMIN"
    login: str
    first_name: str
    second_name: str
    planet: str
    e_mail: str
    pswd: str
    user_type: Roles


class Question(BaseModel):
    question_id: int
    type_question: str
    content: str
    correct_answer: bool


class Answer(BaseModel):
    question_id: int
    user_id: int
    user_answer: str


