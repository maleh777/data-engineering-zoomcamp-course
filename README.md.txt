markdown
# 01 - Docker & Terraform

This module introduces the basics of Docker.

## Project: Simple Pipeline

This project demonstrates a simple Python pipeline running in a Docker container.

### Building the image

1. Navigate to the project directory: `cd 01-docker-terraform`
2. Run the build command: `docker build -f .\docker\Dockerfile -t my-pipeline-image .`

### Running the container

1. Run the container: `docker run -it my-pipeline-image "2025-10-2"` (or without the date if your script doesn't need it).

### Files

* `docker/Dockerfile`: The Dockerfile used to build the image.
* `docker/pipeline.py`: The Python script.
* `docker/requirements.txt`: (If used) The requirements file.
