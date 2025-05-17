from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel, Field, model_validator
from sqlmodel import Session, select
from datetime import date, datetime, time

from ..database import engine, get_db
from ..schema import (
    Reservation,
    ReservationStatus,
)

router = APIRouter(
    prefix="/reservation",
    tags=["reservation"],
    responses={404: {"description": "Not found"}},
)


def is_reservation_in_past(date: date, start_time: int):
    reservation_date = datetime(
        date.year, date.month, date.day, hour=start_time, minute=15
    )

    return reservation_date < datetime.now()


class NewReservation(BaseModel):
    room_searches: Annotated[list[str], Field(..., min_length=1)]
    date: date
    start_time: Annotated[int, Field(..., ge=7, le=21)]
    end_time: Annotated[int, Field(..., ge=8, le=22)]

    @model_validator(mode="after")
    def _(self):
        if self.start_time > self.end_time:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST, "end_time has to be before start_time"
            )

        if is_reservation_in_past(self.date, self.start_time):
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "reservation in the past")

        return self


@router.post("")
def create_reservation(
    new_reservation: NewReservation,
    db: Session = Depends(get_db),  # pyright:ignore[reportCallInDefaultInitializer]
):
    reservation = Reservation(
        user_id=UUID("48eab64b2b024f3ab42f7841461a9a99"),
        room_search=new_reservation.room_searches[0],
        date=new_reservation.date,
        start_time=new_reservation.start_time,
        end_time=new_reservation.end_time,
        status=ReservationStatus.Queued,
    )

    db.add(reservation)
    db.commit()

    # te_auth_type = (TEAuthType.LIU_LOGIN,)
    # te_auth_info = LiuLoginInfo(liu_id="liuid", password="password").model_dump_json()
    return status.HTTP_200_OK
