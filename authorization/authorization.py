from jose import jwt, jws, JWTError
from password_utils import password_utils
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from crud.crud import Crud
from fastapi_jwt_auth import AuthJWT
from crud.schemas import User

crud = Crud()

expires_delta_access = timedelta(seconds=60)
expires_delta_refresh = timedelta(days=30)
SECRET_KEY = "secret"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(user_name: str):
    to_encode = {"user_name": user_name, "type": "access_token"}  # TODO: вместо строки использовать enum
    expires = datetime.utcnow() + expires_delta_access
    to_encode["exp"] = expires
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=password_utils.ALGORITHM)
    return encode_jwt


def create_refresh_token(user_name: str):
    to_encode = {"user_name": user_name, "type": "refresh_token"}
    expires = datetime.utcnow() + expires_delta_refresh
    to_encode["exp"] = expires
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=password_utils.ALGORITHM)
    return encode_jwt


def create_login_token_pair(username: str):
    access_token = create_access_token(username)
    refresh_token = create_refresh_token(username)
    login_token = dict(
        access_token=f"{access_token}",
        refresh_token=f"{refresh_token}"
    )
    return login_token


def decode_access_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        if payload['type'] != "access_token":
            raise HTTPException(status_code=401, detail='Invalid token')
        return payload['user_name']
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Signature has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')


def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        if payload['type'] != "refresh_token":
            raise HTTPException(status_code=401, detail='Invalid token')
        return payload['user_name']
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Signature has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], crud: Crud):
    user_name = decode_access_token(token)
    user = crud.select_user(user_name)
    return user


# def refresh(user: User, Authorize: AuthJWT = Depends()):
#    Authorize.create_refresh_token(user.login,)


if __name__ == "__main__":
    print(get_current_user(
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2JzIiwiZXhwIjoxNjkxMDg1NTYxfQ.LgSzcyVvDHs3OhySFNH_5BPcRevMs7vUGgUgAQYsZMA",
        crud).login)
    # token1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtdXNhIiwiZXhwIjoxNjg3MjEzNDY3fQ.qqRPCEChdJcxRMuTSBAHrb4XMwULWOdIrAKdlEmIU5E"
    # print(datetime.utcnow() + timedelta(minutes=expires_data))
    # print(jwt.decode(token1, SECRET_KEY, algorithms=[password_utils.ALGORITHM]))
    # print(jws.get_unverified_header(token1).keys())

# "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtdXNhIiwiZXhwIjoxNjg3Mjc4MTY3fQ.KBhzxqgQ0SLtUd_I3k7r3dqEy4VM_dm9H-R2ZBYjDvE"
