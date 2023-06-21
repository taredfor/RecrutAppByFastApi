from passlib.context import CryptContext

ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(pass_wd):
    return pwd_context.hash(pass_wd)

#print(hash_password("qwerty"))

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#print(verify_password("qwerty", "$2b$12$NtgaoLxx0yU4j4Q2DarJx.gUFLdhibrRxMNRDWzwJ7sx1/eBaJgQ."))



