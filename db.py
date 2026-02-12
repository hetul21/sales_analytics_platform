from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine("sqlite:///sales.db", echo = True)

Session = sessionmaker(bind=engine)

def create_db():
    Base.metadata.create_all(engine)