from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.items import router as items_router

app = FastAPI()

# Set up CORS middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routes
app.include_router(items_router, prefix="/items", tags=["items"])

# Define root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}