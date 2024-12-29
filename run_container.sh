#!/bin/bash

# Run the Docker container called family_finances with MySQL password
docker run --name family-finances -e MYSQL_ROOT_PASSWORD=DevelopmentPhase -p 3306:3306 -d family-finances:latest