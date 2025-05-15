from enum import Enum
from pydantic import BaseModel
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4
from datetime import date


class TEAuthType(Enum):
    LIU_LOGIN = "liu_login"
    NODE = "node"
    LIU_FS_SESSION = "liu_fs_session"


type TEAuth = LiuLoginAuth | NodeAuth | LiuFsAuth


class LiuLoginAuth(BaseModel):
    te_auth_type: TEAuthType = TEAuthType.LIU_LOGIN
    liu_id: str
    password: str


class NodeAuth(BaseModel):
    te_auth_type: TEAuthType = TEAuthType.NODE
    domain: str


class LiuFsAuth(BaseModel):
    te_auth_type: TEAuthType = TEAuthType.LIU_FS_SESSION
    msis_auth: str


class ReservationStatus(Enum):
    Queued = "queued"
    Cancelled = "cancelled"
    Booked = "booked"


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    username: str = Field(index=True, unique=True, nullable=False)
    password: str = Field(nullable=False)
    te_auth: str | None = Field(default=None)


class AuthSession(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="user.id")


class Reservation(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="user.id")
    room_search: str
    date: date
    start_time: int
    end_time: int
    status: ReservationStatus
