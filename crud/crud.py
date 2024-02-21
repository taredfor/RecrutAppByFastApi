import sqlalchemy
import sqlalchemy.orm
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from .schemas import User, Questions, Answers, UserSchema, HireTypes

from enum import Enum

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
                 user_type: str, hire_type: str):

        add_object = User(login=login,
                          first_name=first_name,
                          second_name=second_name,
                          e_mail=e_mail,
                          planet=planet,
                          pswd_hash=pass_wd,
                          user_type=user_type,
                          hire_type=hire_type
                          )  # TODO: добавить хэштрование
        self.session.add(add_object)
        self.session.commit()

    def delete_user(self, id: int):
        delete_object = self.get_user(id)
        print(delete_object)
        self.session.delete(delete_object)
        self.session.commit()

    def select_user(self, login: str):
        user = select(User.id).where(User.login == login)
        return self.get_user(self.session.scalars(user).first())

    def recrut_exist(self, id: int) -> bool:
        select_statement = select(User).where((User.id == id) & (User.user_type == 'RECRUT'))
        return bool(self.session.execute(select_statement).first())

    def add_question(self, question_id: int, type_question: str, content: str, correct_answer: bool):
        add_object = Questions(question_id=question_id,
                               type_question=type_question,
                               content=content,
                               correct_answer=correct_answer, )
        self.session.add(add_object)
        self.session.commit()

    def add_answer_user(self, question_id: int, your_answer: str, user_id: int):
        question = select(Questions.id).where(Questions.id == question_id)
        correct_answer = self.get_question(self.session.scalars(question).first()).correct_answer
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
        question = select(Questions.id).where(Questions.id == question_id)
        result = self.get_question(self.session.scalars(question).all()).content
        print(result)

    def get_questions_id(self):
        questions = self.session.execute(select(Questions.id)).all()
        result = [i[0] for i in questions]
        return result

    def get_id_from_questions(self, answer: str):
        questions = self.session.execute(select(Questions.question_id).where(Questions.content == answer))
        return questions.first()[0]

    def get_user_id_from_table_answers(self, user_id: int):
        answers = self.session.query(Answers).filter(Answers.user_id == user_id)
        print(answers.all())
        return answers.all()

    def get_user_from_planet_name(self, planet: str):
        user_type_sq = 'RECRUT'
        smth = self.session.query(User).filter((User.user_type == user_type_sq) & (User.planet == planet))
        result = smth.all()
        planet_list = []
        for i in result:
            user = UserSchema(exclude=['pswd_hash', 'e_mail'])
            user_json = user.dump(i)
            user_json["planet"] = user_json["planet"].value
            user_json["user_type"] = user_json["user_type"].value
            planet_list.append(user_json)
        return planet_list

    def get_score(self, recrut_id: int) -> int:
        answers = self.session.query(Answers).filter(Answers.user_id == recrut_id)
        result = 0
        for answer in answers.all():
            if answer.is_correct == "TRUE":
                result += 1
        return result

    def recrut_done_with_test(self, recrut_id: int) -> bool:
        answers = self.session.query(Answers).filter(Answers.user_id == recrut_id)
        return bool(answers.all())

    def hire(self, recrut_id):
        user = self.get_user(recrut_id)
        user.hire_type = HireTypes.HIRED
        self.session.commit()

    def is_email_exist(self, email: str)->bool:
        email_users = self.session.query(User).filter(User.e_mail == email).all()
        return bool(email_users)

    def is_login_exist(self, login: str)->bool:
        users = self.session.query(User).filter(User.login == login).all()
        return bool(users)

if __name__ == "__main__":
    # print(Crud().get_user(1).first_name)
    # Crud().add_user("malk", "Malk", "Malkolm", "sigal@mail.ru", "Brazil", "string", "qwqewrere")
    # Crud().delete_user2("Steve", "Sigal", "sigal@mail.ru")
    # print(Crud().select_user("musa").user_type)
    # print(Crud().get_questions_id())
    # print(Crud().get_id_from_questions("Do you like football"))
    #print(Crud().get_user_id_from_table_answers(7))
    #print(Crud().get_user_from_planet_name('JUPITER'))
    #print(Crud().recrut_done_with_test(12))
    #print(Crud().recrut_done_with_test(20))
    # Crud().add_question(3, "Question", "FALSE", "Do you like boxing")
    # print(Crud().add_answer_user(3, True, 1))
    # print(Crud().add_answer_user(2, 'FALSE', 3))
    # print(Crud().add_answer_user(3, "FALSE", 4))
    # print(Crud().get_all_question(4))
    # print(Crud().get_count_question())
    print(Crud().is_email_exist('mark@123.com'))
    print(Crud().is_email_exist('mark@1234.com'))
    print(Crud().is_login_exist('jobss'))
    print(Crud().is_login_exist('jobssssss'))
    pass
