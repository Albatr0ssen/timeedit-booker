from sqlmodel import SQLModel, Session, create_engine

from src.schema import User

sqlite_file_name = "data/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def reset_db():
    SQLModel.metadata.drop_all(bind=engine)
    create_db_and_tables()


def seed():
    SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(engine)
    user = User(
        username="userman",
        password="securepass",
    )

    with Session(engine) as session:
        session.add(user)
        session.commit()
