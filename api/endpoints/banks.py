from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List  # Import List from typing

from api import crud, schemas
from configs.config import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.Bank])  # Use List from typing
def read_banks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    banks = crud.get_banks(db, skip=skip, limit=limit)
    return banks
