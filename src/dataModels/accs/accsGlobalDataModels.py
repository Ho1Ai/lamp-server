from pydantic import BaseModel

class RegistrationData(BaseModel):
    email: str
    uname: str
    passwd: str

class SignIn(BaseModel):
    email: str
    passwd: str
