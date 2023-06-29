from fastapi import FastAPI, HTTPException
from starlette import status
from enum import Enum

from data_request_model import User, Question, Answer
from crud.crud import Crud
from password_utils.password_utils import hash_password, verify_password
from authorization.authorization import create_access_token, get_current_user
from auxiliary_package.range_function import Range

app = FastAPI()

crud = Crud()
range_func = Range()


@app.get('/')
async def test():
    return {'hello': 'recrut'}


@app.post('/add-user')
async def add_user(parameters: User):
    crud.add_user(parameters.first_name, parameters.second_name, parameters.e_mail, parameters.planet,
                  hash_password(parameters.pswd))
    return 'User is added'


@app.get('/login')
async def verify_password_main(login: str, pass_wd: str):
    credentianals_extensions = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                             detail="UNAUthorized",
                                             headers={"WWW-Authenticate": "Bearer"}, )
    try:
        user = crud.select_user(login).login
        if user is None:
            raise credentianals_extensions
        if verify_password(pass_wd, crud.select_user(login).pswd_hash) is False:
            raise credentianals_extensions
    except:
        raise credentianals_extensions
    return create_access_token(login)


@app.get('/test')
async def test_get_user(token):
    return get_current_user(token, crud)


@app.post('/add/question')
async def add_new_question(parameter: Question):
    crud.add_question(parameter.question_id, parameter.type_question, parameter.content, parameter.correct_answer)
    return 'Question was added'

@app.post('/add/answer')
async def add_answer(parameter: Answer):
    crud.add_answer_user(parameter.question_id, parameter.user_answer, parameter.user_id)
    return 'Answer was sented'

@app.get('/get-questions')
async def get_question():
    d_ict = {}
    j = 1
    count_id = crud.get_count_question()
    list_id = range_func.range_id(count_id)
    for i in list_id:
        d_ict[j] = crud.get_question(i).content
        j += 1
    return d_ict



