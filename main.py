import http
import logging
from fastapi import FastAPI, HTTPException, Header, Depends
from starlette import status
from enum import Enum

from data_request_model import User, Question, Answer, TestAnswer
from crud.crud import Crud
from password_utils.password_utils import hash_password, verify_password
from authorization.authorization import create_access_token, get_current_user
from auxiliary_package.range_function import Range
from typing import Annotated, Union
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from random import choice

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")

app = FastAPI()

crud = Crud()
range_func = Range()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
oauth2_scheme_1 = OAuth2PasswordBearer(tokenUrl="login")


@app.get('/')
async def test():
    return {'hello': 'recrut'}


@app.post('/token')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = crud.select_user(form_data.username).login
    hash_pass = hash_password(form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not verify_password(form_data.password, crud.select_user(user).pswd_hash):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(user)
    return {"access_token": access_token, "token_type": "bearer"}


@app.post('/add-user')
async def add_user(parameters: User):
    crud.add_user(parameters.login, parameters.first_name, parameters.second_name, parameters.e_mail, parameters.planet,
                  hash_password(parameters.pswd), parameters.user_type.value)
    return 'User is added'


@app.get('/login')
async def verify_password_main(login: str, pass_wd: str):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                             detail="UNAUthorized",
                                             headers={"WWW-Authenticate": "Bearer"}, )
    user = crud.select_user(login)
    if not user:
        print(user)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Login not found")
    elif not verify_password(pass_wd, user.pswd_hash):
        print(verify_password(pass_wd, user.pswd_hash))
        print(pass_wd)
        print(login)
        print(crud.select_user(login).pswd_hash)
        raise credentials_exception
    return {"access_token": create_access_token(login)}


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
async def get_question(token: Annotated[str, Depends(oauth2_scheme)]):
    credentianals_extensions = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                             detail="UNAUthorized",
                                             headers={"WWW-Authenticate": "Bearer"}, )
    d_ict = {}
    user = get_current_user(token, crud)
    if not user:
        raise credentianals_extensions
    #count_id = crud.get_count_question()
    question_id = crud.get_questions_id()
    list_id = []
    for i in range(min(len(question_id),3)):
        element = choice(question_id)
        list_id.append(element)
        question_id.remove(element)
    for i in list_id:
        d_ict[i] = crud.get_question(i).content
    return d_ict


@app.get('/items')
async def read_items(user_agent: Annotated[Union[str, None], Header()] = None,
                     authorization: Annotated[Union[str, None], Header()] = None):
    print(user_agent)
    print(authorization)
    return {"User-agent": user_agent, "Authorization": authorization}


@app.get('/role')
async def get_role(token: Annotated[str, Depends(oauth2_scheme)]):
    credentianals_extensions = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                             detail="UNAUthorized",
                                             headers={"WWW-Authenticate": "Bearer"}, )
    user = get_current_user(token, crud)
    if not user:
        raise credentianals_extensions
    return {"user_role": user.user_type}  # TODO: привести переменную к одному знаменателю

@app.post('/post_answers')
async def post_answers_test(test_answer: TestAnswer):
    print(test_answer.questions)
