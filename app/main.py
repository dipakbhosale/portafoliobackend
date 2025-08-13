from fastapi import FastAPI
from app.routes import portfolio

app = FastAPI(title="Portfolio Backend", version="1.0.0")

# Include routes
app.include_router(portfolio.router)

@app.get("/")
def root():
    return {"message": "Portfolio API is running"}
