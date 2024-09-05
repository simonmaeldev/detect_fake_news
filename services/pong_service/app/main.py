from fastapi import FastAPI
from shared_models.pong_models import PongResponse

app = FastAPI()

# service
@app.get("/ping", response_model=PongResponse)
async def ping():
    return PongResponse(text='pong')


# health check
@app.get("/health")
async def health():
    return {"message": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)