import string
import random
from sqlalchemy.orm import Session
from app.core.models.short_urls import ShortURL

def generate_short_code (length: int=8) -> str:
    characters = string.ascii_letters + string.digits

    short_code = "".join(random.choice(characters) for number_of_times in range(length))
    
    return short_code

def create_short_url(db: Session, original_url: str ) -> ShortURL:
    while True:
        short_code = generate_short_code()
        exists = db.query(ShortURL).filter_by(short_url=short_code).first()

        if not exists:
            break

    url = ShortURL(original_url=original_url, short_url=short_code)

    db.add(url)
    db.commit()
    db.refresh(url)

    return url

def get_original_url(db: Session, short_code: str) -> ShortURL | None:
    short_url_object = db.query(ShortURL).filter_by(short_url=short_code).first()

    return short_url_object