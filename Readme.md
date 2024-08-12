# Flask Data Processing Application


## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Running Locally](#running-locally)
  - [Running with Docker](#running-with-docker)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)

## Project Structure
```plaintext
.
├── app.py
├── docker-compose.yml
├── Dockerfile
├── Readme.md
├── requirements.txt
├── static
│   └── swagger.json
├── images
│   ├── image1
│   ├── image2
│   ├── image3
│   └── ...
└── test_app.py
```


## Features

- **Data Retrieval:** Fetches mock data simulating an external API call.
- **Data Processing:** Converts the name field in the data to uppercase.
- **In-memory Storage:** Stores processed data in memory.
- **API Documentation:** Includes a Swagger UI for API documentation.

## Prerequisites

- **Python 3.7+**
- **Docker (if using Docker)**
- **Docker Compose (if using Docker)**

## Setup

### Running Locally

1. **Create a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python app.py 
```
![](/images/Screenshot%202024-08-12%20at%2011.44.00 PM.png)

4. **Access the application:**
Open your browser and go to `http://localhost:5000` or `http://127.0.0.1:5000`
Swagger : `http://localhost:5000/swagger` or `http://127.0.0.1:5000/swagger`


### Running with Docker
1. **Build and run the Docker container:**

```bash
docker-compose up
```
![](/images/Screenshot%202024-08-12%20at%2011.09.23 PM.png)
2. **Access the application:**

Open your browser and go to `http://localhost:5000` or `http://127.0.0.1:5000`
Swagger : `http://localhost:5000/swagger` or `http://127.0.0.1:5000/swagger`

### API Endpoints

- **GET /fetch-data:** Fetch mock data simulating retrieval from an external service.

  **Response:**

  ```json
  [
    {"id": 1, "name": "Product A", "price": 100},
    {"id": 2, "name": "Product B", "price": 150},
    {"id": 3, "name": "Product C", "price": 200}
  ]
  ```

- **POST /process-data:** Process the fetched data and store it in memory.

    **Request Body Example:**

    ```json
    [
    {"id": 1, "name": "Product A", "price": 100},
    {"id": 2, "name": "Product B", "price": 150},
    {"id": 3, "name": "Product C", "price": 200}
    ]
    ```

    **Response Body Example:**
    ```json
    {"message": "Data processed and stored successfully"}
    ```

- **GET /get-processed-data: Retrieve the processed data stored in memory.**

    **Response:**
    ```json
    [
        {"id": 1, "name": "PRODUCT A", "price": 100},
        {"id": 2, "name": "PRODUCT B", "price": 150},
        {"id": 3, "name": "PRODUCT C", "price": 200}
    ]
    ```

### Running Tests

#### Unit tests are included to ensure the application functions as expected.

**Run the tests:**

```bash
python test_app.py
```

> Ensure that the Flask application is not running while you run the tests, as it will start its own instance of the application for testing purposes.
![](/images/Screenshot%202024-08-12%20at%2011.45.15 PM.png)

**Example Test Coverage**
- **Fetch Data Test:** Ensures the /fetch-data endpoint returns the correct mock data.
- **Process Data Test:** Validates that the /process-data endpoint processes and stores the data correctly.
- **Get Processed Data Test:** Confirms that the /get-processed-data endpoint retrieves the processed data accurately.


# Screen Shots
![swagger image](/images/SCR-20240812-ttgw.png)







