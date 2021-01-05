# main.py
from fastapi import Depends, FastAPI
from fastapi import FastAPI, Path, Body, Depends
from sqlalchemy.orm import Session, sessionmaker
from starlette.requests import Request
from db.db import Title, main_engine, punc_engine#, viet_engine, tran_engine
from model.models import TitleOut

# Connect when a session class instance for DB connection is created
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=main_engine)
SessionLocal2 = sessionmaker(autocommit=False, autoflush=False,bind=punc_engine)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=viet_engine)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=tran_engine)



# Utility to get a single Todo
def get_tripitaka(db_session: Session, title_id: int):
    return db_session.query(Title).filter(Title.id == title_id).first()


# Pass the session of DB connection to the function of each endpoint
def get_db(request: Request):
    return request.state.db


app = FastAPI()


@app.get("/tripitakas/")
def read_tripitakas(db: Session = Depends(get_db)): #, response_model=TitleOut):
    """List Tripitakas"""
    tripitakas = db.query(Title).first()
    return tripitakas


@app.get("/tripitakas/{title_id}")
def read_tripitaka(tripitaka_id: int, db: Session = Depends(get_db)):
    """Get a Sutra by id"""
    tripitaka = get_tripitaka(db, tripitaka_id)
    return tripitaka


# @app.post("/todos")
# async def create_todo(todo_in: TodoIn, db: Session = Depends(get_db)):
#     """Create a Todo"""
#     todo = Title(title=todo_in.title, done=False)
#     db.add(todo)
#     db.commit()
#     todo = get_todo(db, todo.id)
#     return todo


# @app.put("/todos/{todo_id}")
# async def update_todo(todo_id: int, todo_in: TodoIn, db: Session = Depends(get_db)):
#     """Update a Todo"""
#     todo = get_todo(db, todo_id)
#     todo.title = todo_in.title
#     todo.done = todo_in.done
#     db.commit()
#     todo = get_todo(db, todo_id)
#     return todo


# @app.delete("/todos/{todo_id}")
# async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
#     """Delete a Todo"""
#     todo = get_todo(db, todo_id)
#     db.delete(todo)
#     db.commit()


# Create a session instance for middleware DB connection which will be called
# for each request
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response
