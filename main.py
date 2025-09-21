from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from database.database_connection import get_database, Base, engine
from database.db_models import Events, DailyAggregate, ModelRegistry 

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Backend Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the Backend Service!"}

@app.get("/health")
def health_check(db: Session = Depends(get_database)):
    try:
        res = db.execute(text("SELECT * FROM events"))
        rows = res.fetchall()
        results = [dict(row._mapping) for row in rows]
        return {"results": results, "database": "healthy"}
    except Exception as e:
        return {"results": "unhealthy", "database": str(e)}