# Use the official MySQL image from the Docker Hub
FROM mysql:latest

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}

# Expose the MySQL port
EXPOSE 3306

# Start MySQL
COPY Database/db_script.sql /docker-entrypoint-initdb.d/
COPY input/master_data.sql /docker-entrypoint-initdb.d/

CMD ["mysqld"]
