from typing import Annotated
from fastapi import APIRouter, Depends, Form, HTTPException, Response
from sqlmodel import Session, select

from ..database import get_db
from ..schema import AuthSession, User


router = APIRouter(
    prefix="",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    response: Response,
    db: Session = Depends(get_db),  # pyright:ignore[reportCallInDefaultInitializer]
):
    user = db.exec(select(User).where(User.username == username)).first()

    if user == None:
        raise HTTPException(status_code=400, detail="incorrect username or password")

    if user.password != password:  # TODO: SHOULD BE HASHED
        raise HTTPException(status_code=400, detail="incorrect username or password")

    auth_session = AuthSession(user_id=user.id)
    db.add(auth_session)
    db.commit()

    response.set_cookie("sid", str(auth_session.id))
    return {"session_token": str(auth_session.id)}
