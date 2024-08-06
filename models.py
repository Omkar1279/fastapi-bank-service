from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from configs.config import Base


class Bank(Base):
    __tablename__ = "banks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    branches = relationship("Branch", back_populates="bank")


class Branch(Base):
    __tablename__ = "branches"
    ifsc = Column(String, primary_key=True, index=True)
    bank_id = Column(Integer, ForeignKey("banks.id"))
    branch = Column(String)
    address = Column(String)
    city = Column(String)
    district = Column(String)
    state = Column(String)

    bank = relationship("Bank", back_populates="branches")
