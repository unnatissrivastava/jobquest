from sqlalchemy import Column, Integer, String, Date
from database import Base

class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, index=True)
    role = Column(String)
    status = Column(String, default="Applied")
    date_applied = Column(Date)
    notes = Column(String, nullable=True)