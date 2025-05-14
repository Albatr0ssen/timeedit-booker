from typing import Annotated
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator
from datetime import date

from sqlmodel import Session

from src.database import engine, reset_db
from src.schema import TEAuthType, User
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


@app.post("/reserve")
def reserve(reservation: Reservation):
    print(reservation.model_dump_json())
    return status.HTTP_200_OK


@app.get("/nuke")
def nuke():
    reset_db()
    return "NUKED"
