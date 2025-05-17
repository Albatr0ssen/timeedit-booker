from fastapi import APIRouter

from ..database import seed

router = APIRouter(
    prefix="",
    tags=["debug"],
    responses={404: {"description": "Not found"}},
)


@router.get("/seed")
def nuke():
    seed()
    return "Database seeded"
