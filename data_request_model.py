from pydantic import BaseModel
from enum import Enum


class User(BaseModel):
    class Roles(Enum): # TODO: сделать единую точку доступа к этому классу
        SITH = "SITH"
        RECRUT = "RECRUT"
        ADMIN = "ADMIN"

    class Planets(Enum): # TODO: сделать единую точку доступа к этому классу
        JUPITER = "JUPITER"
        MARS = "MARS"

    login: str
    first_name: str
    second_name: str
    planet: Planets
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
    user_answer: bool





