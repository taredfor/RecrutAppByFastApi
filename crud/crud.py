import sqlalchemy
import sqlalchemy.orm
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from schemas import User


# engine = create_engine('mysql+mysqldb://root:qwerty123@localhost', pool_recycle=3600)


class Crud():
    def __init__(self):
        self.engine = sqlalchemy.create_engine('mysql+pymysql://root:qwerty123@localhost/Recrut', pool_recycle=3600, echo=True)
        self.conn = self.engine.connect()
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()

    def get_user(self, id):
        self.session.get(User, id)
        return self.session.get(User, id)

    def add_user(self, first_name: str, second_name: str, e_mail: str, planet: str):
        add_object = User(first_name=first_name,
                          second_name=second_name,
                          e_mail=e_mail,
                          planet=planet)
        self.session.add(add_object)
        self.session.commit()

    def delete_user(self, first_name: str, second_name: str, e_mail: str):
        delete_object = self.session.execute(select(User).where(User.first_name == first_name,
                                                                User.second_name == second_name,
                                                                User.e_mail == e_mail)).first()
        self.session.delete(delete_object)
        self.session.commit()

# print(__name__)
if __name__ == "__main__":
    print(Crud().get_user(1).first_name)
   # Crud().add_user("Steve", "Sigal", "sigal@mail.ru", "Siatl")
    Crud().delete_user("Steve", "Sigal", "sigal@mail.ru")
