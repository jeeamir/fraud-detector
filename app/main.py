from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from app.db.session import get_db
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/health")
def health():
    word = "Hello World!"
    print(word)
    return {"status": "ok"}



@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1")).scalar()
        return {"db_status": "ok"}
    except:
        raise HTTPException(status_code= 503, detail="Service unavailable")
