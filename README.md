# detect_fake_news

This project is an implementation of the fake news detection system described in the tutorial at [https://data-flair.training/blogs/advanced-python-project-detecting-fake-news/](https://data-flair.training/blogs/advanced-python-project-detecting-fake-news/).

## Purpose

This project serves as an exercise to train and improve Python programming skills, particularly in the areas of natural language processing and machine learning. It demonstrates how to build a simple fake news detector using Python and various libraries.

## Installation

1. Download the CSV file from [this Google Drive link](https://drive.google.com/file/d/1er9NJTLUA3qnRuyhfzuN0XUsoIC4a-_q/view).
2. Save the downloaded file as `news.csv` in the root directory of this project.
3. You can do both of the above with the following command : `wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1er9NJTLUA3qnRuyhfzuN0XUsoIC4a-_q' -O news.csv.zip && unzip news.csv.zip && rm news.csv.zip`

## Components

- Frontend: Vue 3 (Vite) served by Nginx
- Backend: FastAPI with Uvicorn
- Reverse Proxy: Nginx
- Microservices: Example 'pong' service
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

1. In the `docker-compose.yml` file, change the frontend service to use `Dockerfile` (without `.dev`).
2. In the `backend/Dockerfile`, remove the `"--reload"` : it is useful in dev as it reload the server each time a file change, but use ressources for nothing in prod.
3. Build and run the production environment:

   ```
   docker compose up -d --build
   ```

## API Endpoints

The application provides several endpoints for health checks and basic functionality:

- `/api/ping`: Returns a "pong" response. This demonstrates the communication between the backend and the pong microservice.
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

## Notes

- The template currently responds with "pong" when accessing `/api/ping`, demonstrating the basic structure for microservice communication.
- Modify and expand upon this template to fit your specific application needs.

## Testing the Application

After starting the application, you can test the various endpoints:

1. Ping test: `curl http://localhost/api/ping`
2. Backend health: `curl http://localhost/api/health`
3. System-wide health: `curl http://localhost/api/system-health`
4. Nginx health: `curl http://localhost/nginx-health`

## Troubleshooting

If you encounter any issues:

1. Check if all containers are running: `docker compose ps`
2. View logs of a specific service: `docker compose logs <service_name>`
3. Ensure all required ports are free on your host machine
4. Verify that all services can communicate with each other within the Docker network

## Contributing

Contributions to improve this template are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
