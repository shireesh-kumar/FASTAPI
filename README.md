# FastAPI Todo List Application

This project is a simple FastAPI application designed to store a todo list. While the functionality of the application is basic, the main goal of this project is to build a CI/CD pipeline and deploy the application to an AWS EC2 instance. 

## Features
- **FastAPI**: A simple and fast web framework for building APIs.
- **Dockerized**: The application is containerized using Docker, enabling easy deployment.
- **CI/CD Pipeline**: The pipeline automatically builds and pushes the new Docker image to Docker Hub on every code change (except for `README.md` changes) and deploys the image to an AWS EC2 instance.


## Getting Started

### Prerequisites

- **Docker Desktop** (for Windows users): Docker Desktop needs to be running for Docker to work. For Linux systems, Docker runs natively as a service.
- **Docker Compose**: For running the application using Docker containers.

### Running the Application

### Running via Docker Compose

To run the application with Docker, use the following command to build the image and start the container for the first time:

```bash
docker-compose up --build
```
For later use, you can avoid the --build tag :iykyk

### Running via Uvicorn

If you prefer not to use Docker, you can run the FastAPI app directly using Uvicorn.

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the application**:
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

Note:
- In both Dockerized and local Uvicorn setups, the application will be available at http://localhost:8000 (HTTP, not HTTPS).
- HTTPS configuration requires additional setup and is not included here (to be implemented 😊).


### CI/CD Pipeline
Every time changes are pushed (except for the README.md file), the CI/CD pipeline is triggered. The pipeline performs the following tasks:

- Builds the Docker image using the Dockerfile in the repository.
- Pushes the Docker image to Docker Hub with the latest tag.
- Deployment on AWS EC2 : the image is pulled from Docker Hub to an AWS EC2 instance and run as a Docker container. The application will be available via HTTP at: http://<public-ipv4-ec2>:80


**Note for EC2 Deployment**: 

For those who want to try EC2 deployment, make the following changes in ci-cd.yml file at every occurances:

ubuntu@3.133.122.121 'sudo docker pull shireesh1998/fastapiserver:latest'
In the above command, replace 3.133.122.121 with your EC2 instance's public IPv4 address. Also, shireesh1998 is the Docker Hub username and fastapiserver is the Docker Hub repository name.

You can refer to this medium article for more information: Continuous Deployment with GitHub Actions, DockerHub, and AWS EC2 - A Hands-On Tutorial.

### Conclusion
This project demonstrates the deployment of a simple FastAPI application with an integrated CI/CD pipeline using Docker and AWS EC2


<h6>Acknowledgement: This project briefly refers to the works of https://ashokpoudel.medium.com/ and https://medium.com/@adebisiolayinka30<h6>