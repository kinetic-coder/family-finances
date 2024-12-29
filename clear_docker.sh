#!/bin/bash

# Stop the container
docker stop family-finances

# Remove the container
docker rm family-finances

# Remove the associated images
docker rmi $(docker images -q family-finances)