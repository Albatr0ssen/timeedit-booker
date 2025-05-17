from fastapi import FastAPI
from .routers import auth, debug, reservation, user

app = FastAPI()

app.include_router(auth.router)
app.include_router(debug.router)
app.include_router(user.router)
app.include_router(reservation.router)
