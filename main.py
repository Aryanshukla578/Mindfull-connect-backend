<<<<<<< HEAD
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://mindful-connect-drab.vercel.app",  # your frontend
    "http://localhost:3000",  # local development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for all origins (not recommended for prod)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Continue with your route imports
=======
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://mindful-connect-drab.vercel.app",  # your frontend
    "http://localhost:3000",  # local development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for all origins (not recommended for prod)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Continue with your route imports
>>>>>>> d7d969a4f396dbd6893856d16c4541fb26a331a2
