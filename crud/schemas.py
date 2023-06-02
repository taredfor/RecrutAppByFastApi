from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
Base = declarative_base()

class User(Base):
    __tablename__ = "Users"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    first_name = Column("first_name", String(200))
    second_name = Column("second_name", String(200))
    e_mail = Column("e_mail", String(200))
    planet = Column("planet", String(200))
    pswd_hash = Column("pswd_hash", String(200))