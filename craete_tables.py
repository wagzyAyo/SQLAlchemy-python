from models import Base, User, Comment
from connection import engine


print("CRAETING TABLESS >>> ")
Base.metadata.create_all(bind=engine)
