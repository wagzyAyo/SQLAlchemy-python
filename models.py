from sqlalchemy.orm import declarative_base, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from typing import List

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id: mapped_column[int] = mapped_column(primary_key=True)
    username: mapped_column[str] = mapped_column(nullable=False)
    email_address: mapped_column[str]
    comments: List['Comment'] = relationship(back_populates='user')

    def __repr__(self) -> str:
        return f"<User username={self.username}>"


class Comment(Base):
    __tablename__ = 'comments'
    id: mapped_column[int] = mapped_column(primary_key=True)
    user_id: mapped_column[int] = mapped_column(ForeignKey('users.id'))
    text: mapped_column[str] = mapped_column(Text, nullable=False)
    user: 'User' = relationship(back_populates='comments')

    def __repr__(self) -> str:
        return f"<Comment text={self.text} by {self.user.username}>"
