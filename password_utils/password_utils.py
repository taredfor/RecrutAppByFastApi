from passlib.context import CryptContext

ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(pass_wd):
    return pwd_context.hash(pass_wd)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)