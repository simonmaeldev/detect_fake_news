from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from shared_models.pong_models import PongResponse
import httpx
from typing import Optional
from urllib.parse import urljoin

app = FastAPI()

# for the CORS
origins = [
    "http://localhost",
    "http://localhost:80",
    "http://127.0.0.1",
    "http://127.0.0.1:80",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# same name as the one defined in the docker-compose service
services = {
    'pong': 'http://pong_service:8000'
}

def getUrl(serviceName: str, path: str) -> Optional[str]:
    if serviceName in services:
        return urljoin(services[serviceName], path)
    else:
        return None
    

@app.get("/ping", response_model=PongResponse)
async def ping():
    service_name = 'pong'
    async with httpx.AsyncClient() as client:
        url = getUrl(service_name, 'ping')
        if url :
            response = await client.get(url)
            if response.status_code != 200:
                raise HTTPException(status_code=500, detail=f"pong service error, response: {response}")
            result = response.json()
            return PongResponse(**result)
        else:
            raise HTTPException(status_code=500, detail=f"server error, service name not defined : {service_name}")



@app.get("/health")
async def health():
    return {"message": "healthy"}

@app.get("/system-health")
async def system_health():
    async with httpx.AsyncClient() as client:
        responses = {"backend" : "up"}
        for s, url in services.items():
            try:
                response = await client.get(f"{url}/health")
                res = "up" if response.status_code == 200 else "down"
            except:
                res = "down"
            responses[s] = res
    return responses

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
