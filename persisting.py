from models import User, Comment
from sqlalchemy.orm import Session
from connection import engine


session = Session(bind=engine)
user1 = User(
    username='Tayo',
    email_addresss='Tayo19@gmail.com',
    comment=[
        Comment(text='Hello World!'),
        Comment(text='Whats Popin')
    ]
)

paul = User(
    username='Paul',
    email_addresss='Paul19@gmail.com',
    comment=[
        Comment(text='Hello Planet!'),
        Comment(text='Whats Popin')
    ]
)


Matty = User(
    username='Matty',
    email_addresss='Matty9@gmail.com',
    comment=[
        Comment(text='Hello Heaves!'),
        Comment(text='Whats Popin')
    ]
)

session.add_all([user1, paul, Matty])

session.commit()
