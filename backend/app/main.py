from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from shared_models.pong_models import PongResponse
from shared_models.prediction_models import PredictResponse, PredictionInput
import httpx
from typing import Optional
from urllib.parse import urljoin
from bs4 import BeautifulSoup

app = FastAPI(openapi_url="/openapi.json")

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
    'pong': 'http://pong_service:7999',
    'prediction': 'http://prediction_service:8000'
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

@app.post("/predict", response_model=PredictResponse)
async def predict(input_data: PredictionInput):
    service_name = 'prediction'
    async with httpx.AsyncClient() as client:
        # Check if input_data.text is a URL
        if input_data.text.startswith(('http://', 'https://')):
            try:
                # Use the get_url_content service to fetch the content
                url_content = await get_url_content(input_data.text)
                input_data.text = url_content['content']
            except HTTPException as e:
                raise e
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"An error occurred while fetching URL: {str(e)}")

        url = getUrl(service_name, 'predict')
        if url:
            response = await client.post(url, json=input_data.model_dump())
            if response.status_code != 200:
                raise HTTPException(status_code=500, detail=f"prediction service error, response: {response}")
            result = response.json()
            return PredictResponse(**result)
        else:
            raise HTTPException(status_code=500, detail=f"server error, service name not defined : {service_name}")

@app.get("/get_url_content")
async def get_url_content(url: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            text_content = soup.get_text(separator=' ', strip=True)
            return {"url": url, "content": text_content}
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=f"Error fetching URL: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
