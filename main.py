from typing import Annotated
from fastapi import Depends, FastAPI, Form, HTTPException, Response, status
from pydantic import BaseModel, Field, model_validator
from datetime import date

from sqlmodel import Session, select

from src.database import get_session, seed
from src.schema import AuthSession, User
from src.routers import user

app = FastAPI()

app.include_router(user.router)


@app.get("/")
def get_root():
    return {"Hello", "World"}


class Reservation(BaseModel):
    room_searches: list[str]
    date: date
    start_time: int = Field(..., ge=7, le=21)
    end_time: Annotated[int, Field(..., ge=8, le=22)]

    @model_validator(mode="after")
    def end_time_after_start(self):
        if self.date >= date.today():
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "date is in the past")

        if self.start_time > self.end_time:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST, "end_time has to be before start_time"
            )

        return self


@app.post("/login")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    response: Response,
    session: Session = Depends(  # pyright:ignore[reportCallInDefaultInitializer]
        get_session
    ),
):
    user = session.exec(select(User).where(User.username == username)).first()
    if user == None:
        raise HTTPException(status_code=400, detail="incorrect username or password")

    if user.password != password:  # TODO: SHOULD BE HASHED
        raise HTTPException(status_code=400, detail="incorrect username or password")

    auth_session = AuthSession(user_id=user.id)
    session.add(auth_session)
    session.commit()

    response.set_cookie("sid", str(auth_session.id))
    return {"session_token": str(auth_session.id)}


@app.post("/reserve")
def reserve(reservation: Reservation):
    print(reservation.model_dump_json())
    return status.HTTP_200_OK


@app.get("/seed")
def nuke():
    seed()
    return "Database seeded"
