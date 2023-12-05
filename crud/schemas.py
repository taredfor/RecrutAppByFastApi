from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import Enum as sqlalchemy_enum
from enum import Enum
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

Base = declarative_base()


# TODO: Сделать единую точку доступа к этому классу
class Roles(Enum):
    SITH = "SITH"
    RECRUT = "RECRUT"
    ADMIN = "ADMIN"


class Planets(Enum):
    JUPITER = "JUPITER"
    MARS = "MARS"
# class Status(TypeEngine['str'], Enum):
#     TRUE = "TRUE",
#     FALSE = "FALSE"

class HireTypes(Enum):
    WAITING = "WAITING"
    HIRED = "HIRED"
    NOT_HIRED = "NOT_HIRED"
    NOT_RECRUT = "NOT_RECRUT"

class User(Base):
    __tablename__ = "Users"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    login = Column("login", String(200))
    first_name = Column("first_name", String(200))
    second_name = Column("second_name", String(200))
    e_mail = Column("e_mail", String(200))
    planet = Column("planet", sqlalchemy_enum(Planets))
    pswd_hash = Column("pswd_hash", String(200))
    user_type = Column("user_type", sqlalchemy_enum(Roles))
    hire_type = Column("hire_type", sqlalchemy_enum(HireTypes))


# CREATE TABLE Questions (
#   id int NOT NULL AUTO_INCREMENT,
#   question_id int NOT NULL,
#   type_question varchar(255) DEFAULT NULL,
#   correct_answer ENUM('TRUE','FALSE'),
#   content varchar(255),
#   PRIMARY KEY (id)
# );


class Questions(Base):
    __tablename__ = "Questions"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    question_id = Column("question_id", Integer)
    type_question = Column("type_question", String(200))
    correct_answer = Column("correct_answer", String(200))
    content = Column("content", String(200))


class Answers(Base):
    __tablename__ = "Answers"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    question_id = Column("question_id", Integer)
    user_id = Column("user_id", Integer)
    is_correct = Column("is_correct", String(200))
    def __repr__(self):
        return f'<user_id: {self.user_id}; question_id: {self.question_id}; result: {self.is_correct}>'


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
