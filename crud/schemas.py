from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Enum

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    login = Column("login", String(200))
    first_name = Column("first_name", String(200))
    second_name = Column("second_name", String(200))
    e_mail = Column("e_mail", String(200))
    planet = Column("planet", String(200))
    pswd_hash = Column("pswd_hash", String(200))

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
