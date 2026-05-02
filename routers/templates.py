from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Template

router = APIRouter()

@router.get("/")
def get_templates(db: Session = Depends(get_db)):
    return db.query(Template).all()