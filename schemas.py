from pydantic import BaseModel
from datetime import date
from typing import Optional

# ---------- Job Application Schemas ----------
class JobApplicationCreate(BaseModel):
    company: str
    role: str
    status: Optional[str] = "Applied"
    date_applied: date
    notes: Optional[str] = None

class JobApplicationResponse(JobApplicationCreate):
    id: int

    class Config:
        from_attributes = True

# ---------- User Schemas ----------
class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str