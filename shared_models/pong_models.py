from pydantic import BaseModel

class PongResponse(BaseModel):
    text: str