from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
import models
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Har request ke liye database session dene wala function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Job Tracker API is running!"}

# CREATE - nayi application add karo
@app.post("/applications", response_model=schemas.JobApplicationResponse)
def create_application(application: schemas.JobApplicationCreate, db: Session = Depends(get_db)):
    new_app = models.JobApplication(**application.model_dump())
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app

# READ - saari applications dekho
@app.get("/applications", response_model=list[schemas.JobApplicationResponse])
def get_applications(db: Session = Depends(get_db)):
    return db.query(models.JobApplication).all()

# READ - ek specific application dekho (id se)
@app.get("/applications/{application_id}", response_model=schemas.JobApplicationResponse)
def get_application(application_id: int, db: Session = Depends(get_db)):
    application = db.query(models.JobApplication).filter(models.JobApplication.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application

# UPDATE - application edit karo
@app.put("/applications/{application_id}", response_model=schemas.JobApplicationResponse)
def update_application(application_id: int, updated: schemas.JobApplicationCreate, db: Session = Depends(get_db)):
    application = db.query(models.JobApplication).filter(models.JobApplication.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    for key, value in updated.model_dump().items():
        setattr(application, key, value)
    db.commit()
    db.refresh(application)
    return application

# DELETE - application hatao
@app.delete("/applications/{application_id}")
def delete_application(application_id: int, db: Session = Depends(get_db)):
    application = db.query(models.JobApplication).filter(models.JobApplication.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(application)
    db.commit()
    return {"message": "Application deleted successfully"}