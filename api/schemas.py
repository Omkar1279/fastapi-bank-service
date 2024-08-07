from pydantic import BaseModel
from typing import List  # Import List from typing


class Bank(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # Updated config key


class Branch(BaseModel):
    ifsc: str
    bank_id: int
    branch: str
    address: str
    city: str
    district: str
    state: str

    class Config:
        from_attributes = True  # Updated config key
