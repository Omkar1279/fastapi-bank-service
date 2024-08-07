# Use the official PostgreSQL image from the Docker Hub
FROM postgres:latest

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=mysecretpassword
ENV POSTGRES_DB=bankdb

# Copy the SQL script into the Docker image
COPY indian_banks.sql /docker-entrypoint-initdb.d/

# Expose port 5432
EXPOSE 5432
