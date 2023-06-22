from pydantic import BaseModel
from enum import Enum

class User(BaseModel):
    #login: str
    first_name: str
    second_name: str
    planet: str
    e_mail: str
    pswd: str


class Question(BaseModel):
    question_id: int
    type_question: str
    content: str
    correct_answer: str


