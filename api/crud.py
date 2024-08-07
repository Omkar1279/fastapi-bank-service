from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.orm import Session

from api.models import Bank, Branch


def get_banks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Bank).offset(skip).limit(limit).all()


def get_branch_by_ifsc(db: Session, ifsc: str):
    return db.query(Branch).filter(Branch.ifsc == ifsc).first()


def get_branches_by_bank(db: Session, bank_id: int, skip: int = 0, limit: int = 10):
    return db.query(Branch).filter(Branch.bank_id == bank_id).offset(skip).limit(limit).all()