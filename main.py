from fastapi import FastAPI

app = FastAPI(title="CodeNinja FastAPI", description="A FastAPI application created by CodeNinja", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Hello from CodeNinja FastAPI!"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
