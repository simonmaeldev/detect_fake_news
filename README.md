# detect_fake_news

This project is an implementation of the fake news detection system described in the tutorial at [https://data-flair.training/blogs/advanced-python-project-detecting-fake-news/](https://data-flair.training/blogs/advanced-python-project-detecting-fake-news/).

## Purpose

This project serves as an exercise to train and improve Python programming skills, particularly in the areas of natural language processing and machine learning. It demonstrates how to build a simple fake news detector using Python and various libraries.

Note: the predictions could be better, but it wasn't the main goal of this project.

## Installation

1. Download the CSV file from [this Google Drive link](https://drive.google.com/file/d/1er9NJTLUA3qnRuyhfzuN0XUsoIC4a-_q/view).
2. Save the downloaded file as `news.csv` in the root directory of this project.
3. You can do both of the above with the following command : `cd services/prediction_service && ./download_data.sh && cd -`

## Components

- Frontend: Vue 3 (Vite) served by Nginx
- Backend: FastAPI with Uvicorn
- Reverse Proxy: Nginx
- Microservice: predict to predict if informations in text or website are fake or real.
- Everything is dockerized for easy deployment and scaling

## Build and Run

### Development

1. Ensure Docker and Docker Compose are installed on your system.
2. Clone this repository.
3. In the `docker-compose.yml` file, verify that the frontend service uses `Dockerfile.dev`.
4. Run the following command to start the development environment:

   ```
   docker compose up -d
   ```

5. To stop the services:

   ```
   docker compose down
   ```

### Production

Build and run the production environment:

```
docker compose up -d --build
```

## API Endpoints

The application provides several endpoints for health checks and basic functionality:

- `/api/docs`: Return the doc with all the services available.
- `/api/health`: Backend health check endpoint.
- `/api/system-health`: Checks the health of all services (backend and microservices).
- `/nginx-health`: Nginx health check endpoint.

## Health Check URLs

To check the health of different components:

1. Nginx Reverse Proxy: `http://localhost/nginx-health`
2. Backend API: `http://localhost/api/health`
3. System-wide health: `http://localhost/api/system-health`
4. Frontend Nginx: `http://localhost/nginx-health`

## Scalability

This template is structured to be scalable. You can add more microservices by:

1. Creating a new service directory under `services/`
2. Adding the service to the `docker-compose.yml` file
3. Updating the `backend/app/main.py` to include routing to the new service

Remember to update the README as you add new services or endpoints.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
