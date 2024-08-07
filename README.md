# FastAPI Bank Service

A FastAPI application for managing bank and branch information. This service provides endpoints to retrieve bank details and branch information using standard REST API practices.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Testing](#testing)
- [Docker](#docker)

## Features

- Retrieve bank information
- Fetch branches by bank ID
- Retrieve branch details by IFSC code

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/fastapi-bank-service.git
   cd fastapi-bank-service
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment:**

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the FastAPI Application:**

   ```bash
   uvicorn main:app --reload
   ```

   The application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

2. **Access the Swagger UI:**

   Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the interactive API documentation.

3. **Access the ReDoc UI:**

   Navigate to [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) for the alternative documentation view.

## Endpoints

### Get Branches by Bank ID

- **URL:** `/branches/by_bank/{bank_id}`
- **Method:** `GET`
- **URL Params:**
  - `bank_id` (int): ID of the bank.
- **Query Params:**
  - `skip` (int, optional): Number of items to skip (default is 0).
  - `limit` (int, optional): Number of items to return (default is 10).
- **Response:**
  - Returns a list of branches.

### Get Branch by IFSC Code

- **URL:** `/branches/by_ifsc/{ifsc}`
- **Method:** `GET`
- **URL Params:**
  - `ifsc` (str): IFSC code of the branch.
- **Response:**
  - Returns details of the branch.

## Testing

1. **Install Test Dependencies:**

   ```bash
   pip install pytest
   ```

2. **Run Tests:**

   ```bash
   pytest
   ```

   The test cases are located in the `tests` directory.

Sure! Here's a section you can add to your `README.md` file to describe the Docker setup for your FastAPI project, including the Dockerfile for PostgreSQL:

---

## Docker Setup

This project includes a Docker setup for running a PostgreSQL database. The `Dockerfile` provided sets up a PostgreSQL instance with a default configuration and initializes it with an SQL script.

### PostgreSQL Dockerfile

The `Dockerfile` for PostgreSQL is designed to:

- Use the official PostgreSQL image from Docker Hub.
- Set up environment variables for PostgreSQL user, password, and database.
- Copy an SQL initialization script into the Docker image to set up the database schema.

#### `Dockerfile`

```Dockerfile
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
```

### Building and Running the PostgreSQL Docker Container

1. **Build the Docker Image:**

   Navigate to the directory containing your `Dockerfile` and build the image with:

   ```bash
   docker build -t my-postgres-db .
   ```

2. **Run the Docker Container:**

   Run the container using:

   ```bash
   docker run -d -p 5432:5432 --name postgres-db my-postgres-db
   ```

   This will start a PostgreSQL container named `postgres-db` and map port 5432 on your host to port 5432 in the container.

### Connecting to PostgreSQL

You can connect to your PostgreSQL database using any PostgreSQL client with the following credentials:

- **Host:** `localhost`
- **Port:** `5432`
- **User:** `postgres`
- **Password:** `mysecretpassword`
- **Database:** `bankdb`

### SQL Initialization Script

The `indian_banks.sql` script located in the Docker context directory is copied into `/docker-entrypoint-initdb.d/` inside the container. This script is automatically executed during container startup to initialize the database schema.
