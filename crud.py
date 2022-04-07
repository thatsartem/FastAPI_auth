from sqlalchemy.orm import Session
from passlib.context import CryptContext


import models
import schemas


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserIn):
    hashed_password = get_password_hash(user.password)
    user_db = models.User(username=user.username,
                          hashed_password=hashed_password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return(user_db)
