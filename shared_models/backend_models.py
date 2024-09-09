from pydantic import BaseModel

class UrlContentResponse(BaseModel):
    url: str
    content: str
