import sqlalchemy
import sqlalchemy.orm
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from .schemas import User


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

    def add_user(self, login: str, first_name: str, second_name: str, e_mail: str, planet: str, pass_wd: str):
        add_object = User(login=login,
                          first_name=first_name,
                          second_name=second_name,
                          e_mail=e_mail,
                          planet=planet,
                          pswd_hash=pass_wd)#TODO: добавить хэштрование
        self.session.add(add_object)
        self.session.commit()

    def delete_user(self, id: int):
        delete_object = self.get_user(id)
        print(delete_object)
        self.session.delete(delete_object)
        self.session.commit()

    # def delete_user2(self, first_name: str, second_name: str, e_mail: str):
    #     delete_object = self.session.execute(select(User).where(User.first_name == first_name)).first()
    #     print((delete_object))
    #     self.session.delete(delete_object)
    #     self.session.commit()
    def select_user(self, login: str):
        stmt = select(User.id).where(User.login == login)
        return self.get_user(self.session.scalars(stmt).first())


# print(__name__)
if __name__ == "__main__":
   # print(Crud().get_user(1).first_name)
    #Crud().add_user("Steve", "Sigal", "sigal@mail.ru", "Siatl")
    #Crud().delete_user2("Steve", "Sigal", "sigal@mail.ru")
    print(Crud().select_user("musa1").pswd_hash)

# items = {"foo": "The Foo Wrestlers"}
# item_id = "foo"
# if item_id in items:
#     print(items[item_id])

