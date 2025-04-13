from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

app = FastAPI()

origins = [
    "https://mindful-connect-drab.vercel.app",  # frontend
    "http://localhost:3000",  # local dev
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔁 Redirect root to frontend
@app.get("/")
async def redirect_to_frontend():
    return RedirectResponse(url="https://mindful-connect-drab.vercel.app")

# 👇 Import your other routes below this
# from routes import your_endpoints
