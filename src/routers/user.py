from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, model_validator
from sqlmodel import Session

from src.database import engine
from src.schema import LiuFsAuth, LiuLoginAuth, NodeAuth, TEAuth, TEAuthType, User


def true_func():
    return False


router = APIRouter(
    prefix="/user",
    tags=["user"],
    dependencies=[Depends(true_func)],
    responses={404: {"description": "Not found"}},
)


class NewUser(BaseModel):
    username: str
    password: str


@router.post("")
def add_user(new_user: NewUser):
    user = User(
        username=new_user.username,
        password=new_user.password,
    )
    with Session(engine) as session:
        session.add(user)
        session.commit()

    # te_auth_type = (TEAuthType.LIU_LOGIN,)
    # te_auth_info = LiuLoginInfo(liu_id="liuid", password="password").model_dump_json()
    return status.HTTP_200_OK


@router.put("/te-auth")
def update_auth(te_auth: LiuLoginAuth | NodeAuth | LiuFsAuth):
    return te_auth.model_dump_json()
