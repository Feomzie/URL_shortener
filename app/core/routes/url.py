from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import session_local
from app.core.services.url_services import generate_short_code, create_short_url
from app.core.schemas.url import URLCreate, URLResponse


router = APIRouter()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@router.post("/shorten", response_model=URLResponse)
def shorten_url(input:URLCreate, db: Session =  Depends(get_db)):
    url = create_short_url(db, input.original_url)

    return {
        "short_url": url.short_url
    }