from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from .database import engine, SessionLocal
from .models import Base, Donation, Request
from .schemas import DonationCreate, DonationResponse, RequestCreate, RequestResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Food Donation Platform")

app.mount("/static", StaticFiles(directory="static"), name="static")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/donations", response_model=DonationResponse)
def create_donation(donation: DonationCreate, db: Session = Depends(get_db)):
    new_donation = Donation(**donation.model_dump())
    db.add(new_donation)
    db.commit()
    db.refresh(new_donation)
    return new_donation


@app.get("/donations", response_model=list[DonationResponse])
def list_donations(db: Session = Depends(get_db)):
    return db.query(Donation).all()


@app.patch("/donations/{donation_id}/claim", response_model=DonationResponse)
def claim_donation(donation_id: int, db: Session = Depends(get_db)):
    donation = db.query(Donation).filter(Donation.id == donation_id).first()
    if not donation:
        raise HTTPException(status_code=404, detail="Donation not found")

    donation.status = "claimed"
    db.commit()
    db.refresh(donation)
    return donation


@app.post("/requests", response_model=RequestResponse)
def create_request(request: RequestCreate, db: Session = Depends(get_db)):
    new_request = Request(**request.model_dump())
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request


@app.get("/requests", response_model=list[RequestResponse])
def list_requests(db: Session = Depends(get_db)):
    return db.query(Request).all()