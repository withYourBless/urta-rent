from sqlalchemy.orm import Session

from urtaApi import models, repositories
from urtaApi.dsn import SessionLocal, engine

from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from jwt.exceptions import InvalidTokenError

from urtaApi import dto
from urtaApi.security import oauth2_scheme, ALGORITHM, SECRET_KEY, TokenData


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionDep = Annotated[Session, Depends(get_db)]


async def get_current_user(session: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        phone: str = payload.get("sub")
        if phone is None:
            raise credentials_exception
        token_data = TokenData(login=phone)
    except InvalidTokenError:
        raise credentials_exception
    user = repositories.get_owner_by_phone_number(phone=token_data.login)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
        current_user: Annotated[dto.Owner, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

CurrentActiveUser = Annotated[models.Owner, Depends(get_current_active_user)]
