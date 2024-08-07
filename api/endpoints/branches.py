from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api import crud, schemas
from configs.config import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/by_bank/{bank_id}", response_model=List[schemas.Branch])
def read_branches(bank_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    branches = crud.get_branches_by_bank(db, bank_id=bank_id, skip=skip, limit=limit)
    if branches is None:
        raise HTTPException(status_code=404, detail="Branches not found")
    return branches


@router.get("/by_ifsc/{ifsc}", response_model=schemas.Branch)
def read_branch(ifsc: str, db: Session = Depends(get_db)):
    branch = crud.get_branch_by_ifsc(db, ifsc=ifsc)
    if branch is None:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch
