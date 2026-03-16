from pydantic import BaseModel
from typing import Optional


class DonationCreate(BaseModel):
    donor_name: str
    food_item: str
    quantity: str
    expiry_date: Optional[str] = None
    location: str


class DonationResponse(BaseModel):
    id: int
    donor_name: str
    food_item: str
    quantity: str
    expiry_date: Optional[str]
    location: str
    status: str

    class Config:
        from_attributes = True


class RequestCreate(BaseModel):
    requester_name: str
    needed_item: str
    quantity: str
    location: str
    notes: Optional[str] = None


class RequestResponse(BaseModel):
    id: int
    requester_name: str
    needed_item: str
    quantity: str
    location: str
    notes: Optional[str]

    class Config:
        from_attributes = True