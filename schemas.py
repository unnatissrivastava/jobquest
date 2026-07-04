from pydantic import BaseModel
from datetime import date
from typing import Optional

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