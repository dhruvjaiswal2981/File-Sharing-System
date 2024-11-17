### File Sharing System

- A simple file-sharing system built with FastAPI and SQLAlchemy, using SQLite as the database. This project provides APIs to upload and retrieve file information, demonstrating the basic CRUD operations with a relational database.

## Features

- Add new file records with filename and file URL.
- Retrieve file information by ID.
- Fully documented API with Swagger and ReDoc.
- SQLite database integration for easy setup.

## Installation

1. Clone the Repository

    ```bash
    git clone https://github.com/dhruvjaiswal2981/File-Sharing-System.git
    cd file-sharing-system

2. Install Dependencies

- Use the requirements.txt file to install all required dependencies:
    
    ```bash
    pip install -r requirements.txt

3. Run the Application

- Start the FastAPI server with Uvicorn:

    ```bash
    uvicorn main:app --reload


## Project Structure

file_sharing_system/
├── main.py           # Main FastAPI application
├── database.py       # Database configuration and connection
├── models.py         # SQLAlchemy models
├── schemas.py        # Pydantic schemas for request/response validation
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation


## API Endpoints

- Base URL
    - Local Development: http://127.0.0.1:8000

## Available Endpoints

1. Create a File Record
    - Endpoint: POST /files/
    - Request Body:
    ```json
    {
    "filename": "example.txt",
    "file_url": "http://example.com/example.txt"
    }

- Response:
    ```json
    {
    "id": 1,
    "filename": "example.txt",
    "file_url": "http://example.com/example.txt"
    }

2. Retrieve a File Record
    - Endpoint: GET /files/{file_id}
    - Path Parameter:
    - file_id: ID of the file to retrieve.
    - Response:
    ```json
    {
    "id": 1,
    "filename": "example.txt",
    "file_url": "http://example.com/example.txt"
    }

3. API Documentation
    - Swagger UI: http://127.0.0.1:8000/docs
    - ReDoc: http://127.0.0.1:8000/redoc

## Running Tests

- To test the endpoints:

    1. Use tools like Postman or cURL.
    2. Alternatively, interact directly with the Swagger UI at http://127.0.0.1:8000/docs.


