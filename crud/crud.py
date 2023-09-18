import enum

import sqlalchemy
import sqlalchemy.orm
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from .schemas import User, Questions, Answers
from enum import Enum


# engine = create_engine('mysql+mysqldb://root:qwerty123@localhost', pool_recycle=3600)

class Crud():
    def __init__(self):
        self.engine = sqlalchemy.create_engine('mysql+pymysql://root:qwerty123@localhost/Recrut', pool_recycle=3600,
                                               echo=False)  # логи sqlalchemy
        self.conn = self.engine.connect()
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()

    def get_user(self, id):
        return self.session.get(User, id)

    def get_question(self, question_id):
        return self.session.get(Questions, question_id)

    def add_user(self, login: str, first_name: str, second_name: str, e_mail: str, planet: str, pass_wd: str,
                 user_type: str):

        add_object = User(login=login,
                          first_name=first_name,
                          second_name=second_name,
                          e_mail=e_mail,
                          planet=planet,
                          pswd_hash=pass_wd,
                          user_type=user_type,
                          )  # TODO: добавить хэштрование
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
        # self.session.close()
        return self.get_user(self.session.scalars(stmt).first())

    def add_question(self, question_id: int, type_question: str, content: str, correct_answer: bool):
        add_object = Questions(question_id=question_id,
                               type_question=type_question,
                               content=content,
                               correct_answer=correct_answer, )
        self.session.add(add_object)
        self.session.commit()

    def add_answer_user(self, question_id: int, your_answer: str, user_id: int):
        smth = select(Questions.id).where(Questions.id == question_id)
        print(type(smth))
        correct_answer = self.get_question(self.session.scalars(smth).first()).correct_answer
        print(correct_answer)
        if correct_answer == your_answer:
            add_object = Answers(question_id=question_id,
                                 user_id=user_id,
                                 is_correct="TRUE"
                                 )
            self.session.add(add_object)
            self.session.commit()
        else:
            add_object = Answers(question_id=question_id,
                                 user_id=user_id,
                                 is_correct="FALSE"
                                 )
            self.session.add(add_object)
            self.session.commit()

    def get_count_question(self):
        count_question = self.session.query(Questions).count()
        return count_question

    def get_all_question(self, question_id: int):
        smth = select(Questions.id).where(Questions.id == question_id)
        result = self.get_question(self.session.scalars(smth).all()).content
        print(result)

    def get_user_role(self, login: str):  ## написано для чего то, если не будет применения то нужно удалить
        return self.select_user(login).user_type

    def get_questions_id(self):
        result = []
        # smth = self.session.query(Questions.id).all()
        smth = self.session.execute(select(Questions.id)).all()
        result = [i[0] for i in smth]

        # print(result)
        # print(smth1)
        return result

    def get_id_from_questions(self, answer: str):
        smth = self.session.execute(select(Questions.question_id).where(Questions.content == answer))
        return smth.first()[0]

    def get_user_id_from_table_answers(self, user_id: int):
        smth = self.session.execute(select(Answers.user_id).where(Answers.user_id == user_id))
        return bool(smth.first()[0])

    def get_user_from_planet_name(self, planet: str):
        user_type_sq = 'RECRUT'
        smth = self.session.query(User).filter((User.user_type == user_type_sq) & (User.planet == planet))
        result = smth.all()
        planet_list = []
        print(result)
        for i in result:
            print(i)
            user_name = i.login
            user_planet_test = i.planet.value
            user_role = i.user_type.value
            print(user_planet_test)
            planet_list.append({"user_name": user_name, "user_planet": user_planet_test, "user_role": user_role})
        print(planet_list)
        return planet_list
# print(__name__)
if __name__ == "__main__":
    # print(Crud().get_user(1).first_name)
    # Crud().add_user("malk", "Malk", "Malkolm", "sigal@mail.ru", "Brazil", "string", "qwqewrere")
    # Crud().delete_user2("Steve", "Sigal", "sigal@mail.ru")
    # print(Crud().select_user("musa").user_type)
    # print(Crud().get_questions_id())
    # print(Crud().get_id_from_questions("Do you like football"))
    #print(Crud().get_user_id_from_table_answers(7))
    print(Crud().get_user_from_planet_name('JUPITER'))
    # Crud().add_question(3, "Question", "FALSE", "Do you like boxing")
    # print(Crud().add_answer_user(3, True, 1))
    # print(Crud().add_answer_user(2, 'FALSE', 3))
    # print(Crud().add_answer_user(3, "FALSE", 4))
    # print(Crud().get_all_question(4))
    # print(Crud().get_count_question())
# items = {"foo": "The Foo Wrestlers"}
# item_id = "foo"
# if item_id in items:
#     print(items[item_id])
