from fastapi import FastAPI
from data_request_model import User
from crud.crud import Crud
from password_utils.password_utils import hash_password, verify_password

app = FastAPI()

crud = Crud()


@app.get('/')
async def test():
    return {'hello': 'recrut'}


@app.post('/add-user')
async def add_user(parameters: User):
    crud.add_user(parameters.login, parameters.first_name, parameters.second_name, parameters.e_mail, parameters.planet,
                  hash_password(parameters.pswd))
    return 'User is added'


@app.get('/login')
async def verify_password_main(login: str, pass_wd: str):
    try:
        if crud.select_user(login).login:
            if verify_password(pass_wd, crud.select_user(login).pswd_hash):
                return 'User authorized successfully'
            else:
                return 'Password is not correct'
    except:
        return 'Login Not Found'
