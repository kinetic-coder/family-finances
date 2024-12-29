#!/bin/bash

# Set the image name
IMAGE_NAME="family-finances"

# Build the Docker image
docker build -t $IMAGE_NAME .