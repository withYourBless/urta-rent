from datetime import datetime, timedelta, timezone

import jwt
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import BaseModel

from urtaApi import repositories

# openssl rand -hex 32
SECRET_KEY = "f1129a024d8ce95ba895d3d90658ce52f5d20bb964df26e90ab490c267fa3edd"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    login: str | None = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_owner(phone: str, password: str):
    owner = repositories.get_owner_by_phone_number(phone)
    if not owner:
        return False
    if not verify_password(password, owner.password):
        return False
    return owner


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
