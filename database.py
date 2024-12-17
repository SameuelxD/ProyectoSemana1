from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///tasks.db"

engine = create_engine(DATABASE_URL, echo=False)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
