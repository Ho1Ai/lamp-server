from pydantic import BaseModel

class TokenData(BaseModel):
    id: int
    email: str
    uname: str
