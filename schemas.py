from pydantic import BaseModel


class Bank(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Branch(BaseModel):
    ifsc: str
    bank_id: int
    branch: str
    address: str
    city: str
    district: str
    state: str

    class Config:
        orm_mode = True
