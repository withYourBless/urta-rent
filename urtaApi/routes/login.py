from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from urtaApi import dto
from urtaApi.deps import CurrentActiveUser
from urtaApi.security import authenticate_owner, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, Token

router = APIRouter()


@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    owner = authenticate_owner(form_data.username, form_data.password)
    if not owner:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": owner.phone_number}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/users/me/", response_model=dto.Owner)
async def read_users_me(
        current_user: CurrentActiveUser):
    return current_user
