from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, database, services
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/fetch-jokes/")
async def fetch_and_store_jokes(amount: int = 100, db: Session = Depends(database.get_db)):
    try:
        # Fetch jokes from API
        jokes = await services.fetch_jokes(amount)
        
        # Process and store jokes
        for joke_data in jokes:
            processed_joke = services.process_joke(joke_data)
            db_joke = models.Joke(**processed_joke)
            db.add(db_joke)
        
        db.commit()
        return {"message": f"Successfully fetched and stored {len(jokes)} jokes"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/jokes/")
def get_jokes(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    jokes = db.query(models.Joke).offset(skip).limit(limit).all()
    return jokes