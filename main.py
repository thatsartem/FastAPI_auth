from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserIn, db: Session = Depends(get_db)):
    user_db = crud.get_user_by_username(db, user.username)
    if user_db:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_user(db, user)


@app.get("/users/", response_model=List[schemas.User])
def get_all_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users
