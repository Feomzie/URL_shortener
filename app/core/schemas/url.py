from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    original_url: str

class URLResponse(BaseModel):
    short_url: str