
from fastapi import FastAPI,Depends
from .database import engine
from . import models
from . routers import post,user,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


print(settings.database_username)

#models.Base.metadata.create_all(bind=engine)
    

app = FastAPI()

orgins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=orgins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get('/')
def ROOT():
    print("hi")
    return "/docs for documentation"











