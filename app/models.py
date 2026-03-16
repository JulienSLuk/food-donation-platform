from sqlalchemy import Column, Integer, String, Text
from .database import Base


class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True, index=True)
    donor_name = Column(String, nullable=False)
    food_item = Column(String, nullable=False)
    quantity = Column(String, nullable=False)
    expiry_date = Column(String, nullable=True)
    location = Column(String, nullable=False)
    status = Column(String, default="available")


class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    requester_name = Column(String, nullable=False)
    needed_item = Column(String, nullable=False)
    quantity = Column(String, nullable=False)
    location = Column(String, nullable=False)
    notes = Column(Text, nullable=True)