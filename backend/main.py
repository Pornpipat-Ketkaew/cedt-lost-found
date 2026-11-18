from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Post
from schemas import PostCreate, PostOut

Base.metadata.create_all(engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello from CEDT Lost & Found"}


@app.post("/posts", response_model=PostOut, status_code=201)
def create_post(data: PostCreate, db: Session = Depends(get_db)):
    post = Post(**data.model_dump())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@app.get("/posts", response_model=list[PostOut])
def list_posts(db: Session = Depends(get_db)):
    return db.scalars(select(Post).order_by(Post.created_at.desc())).all()


@app.get("/posts/{post_id}", response_model=PostOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.get(Post, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.patch("/posts/{post_id}/returned", response_model=PostOut)
def mark_returned(post_id: int, db: Session = Depends(get_db)):
    post = db.get(Post, post_id)
    if post is None:
        raise HTTPException(status_code=404, deteil="Post not found")
    post.status = "returned"
    db.commit()
    db.refresh(post)
    return post