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

expires_data = 15
SECRET_KEY = "secret"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(user_name):
    to_encode = {"sub": user_name}
    expires = datetime.utcnow() + timedelta(minutes=expires_data)
    to_encode["exp"] = expires
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=password_utils.ALGORITHM)
    print()
    return encode_jwt


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], crud: Crud):
    credentianals_extensions = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                             detail="UNAUthorized",
                                             headers={"WWW-Authenticate": "Bearer"}, )

    payload = jwt.decode(token, SECRET_KEY, algorithms=[password_utils.ALGORITHM])
    print(f'payload:{payload}')
    user = crud.select_user(payload["sub"])
    return user

#def refresh(user: User, Authorize: AuthJWT = Depends()):
#    Authorize.create_refresh_token(user.login,)


if __name__ == "__main__":
    print(get_current_user(
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtdXNhIiwiZXhwIjoxNjg3MjEzNDY3fQ.qqRPCEChdJcxRMuTSBAHrb4XMwULWOdIrAKdlEmIU11",
        crud).login)
    #token1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtdXNhIiwiZXhwIjoxNjg3MjEzNDY3fQ.qqRPCEChdJcxRMuTSBAHrb4XMwULWOdIrAKdlEmIU5E"
    #print(datetime.utcnow() + timedelta(minutes=expires_data))
    #print(jwt.decode(token1, SECRET_KEY, algorithms=[password_utils.ALGORITHM]))
    #print(jws.get_unverified_header(token1).keys())



#"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtdXNhIiwiZXhwIjoxNjg3Mjc4MTY3fQ.KBhzxqgQ0SLtUd_I3k7r3dqEy4VM_dm9H-R2ZBYjDvE"
