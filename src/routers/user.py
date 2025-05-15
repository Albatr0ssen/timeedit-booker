from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel, model_validator
from sqlmodel import Session, select

from src.database import engine, get_db
from src.schema import LiuFsAuth, LiuLoginAuth, NodeAuth, TEAuth, TEAuthType, User

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


class NewUser(BaseModel):
    username: str
    password: str


@router.post("")
def create_user(
    new_user: NewUser,
    session: Session = Depends(
        get_db
    ),  # pyright:ignore[reportCallInDefaultInitializer]
):
    statement = select(User).where(User.username == new_user.username)
    if session.exec(statement).first() != None:
        raise HTTPException(status_code=400, detail="username already taken")

    user = User(
        username=new_user.username,
        password=new_user.password,
    )
    session.add(user)
    session.commit()

    # te_auth_type = (TEAuthType.LIU_LOGIN,)
    # te_auth_info = LiuLoginInfo(liu_id="liuid", password="password").model_dump_json()
    return status.HTTP_200_OK


@router.put("/te-auth")
def update_auth(
    te_auth: LiuLoginAuth | NodeAuth | LiuFsAuth,
    session: Session = Depends(
        get_db
    ),  # pyright:ignore[reportCallInDefaultInitializer]
):

    # Get user using depends or somehting
    # Update user with new te_auth

    session.commit()

    return te_auth.model_dump_json()
