from sqlmodel import SQLModel, create_engine

sqlite_file_name = "data/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def reset_db():
    SQLModel.metadata.drop_all(bind=engine)
    create_db_and_tables()


if __name__ == "__main__":
    reset_db()
