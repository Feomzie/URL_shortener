from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

from app.db.database import session_local
from app.core.services.url_services import generate_short_code, create_short_url, get_original_url
from app.core.schemas.url import URLCreate, URLResponse

from app.config.settings import settings


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
        "short_url": f"{settings.BASE_URL}{url.short_url}"
    }


@router.get("/{short_code}")
def redirect(short_code: str, db: Session = Depends(get_db)):
    url = get_original_url(db, short_code)

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return RedirectResponse(url.original_url)
