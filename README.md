# Stacker2X
Stacker2X is a simple Django-based Number Classification API that returns a JSON response containing properties of a number, like its primality, parity, A fun fact etc.

## Features
- Responds to `GET` requests with a JSON object.
- Returns the number, its primality, parity, sum of its digits, whether Amstrong, its perfectness and a fun    fact about the number

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python (>= 3.11)
- pip (Python package manager)


### Installation
1. Clone the repository:
   ```sh
    git clone https://github.com/charlesigboanugo/Stacker2x.git
    cd Stacker2X

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install dependencies:
    ```sh
    pip install -r requirements.txt

4. Run Migrations
    ```sh
    python manage.py migrate

5. Start the development server:
    ```sh
    python manage.py runserver

If used for production

    Start the production server:
    ```sh
    gunicorn api.wsgi:application

The API will be accessible at http://127.0.0.1:8000/.


# API Documentation

## Endpoint
    GET /api/classify-numbers?numbers=<integer>

    Request
        Method: GET
        Headers: NoNE
        Body: None

    Response
        Status: 200 OK
        Content-Type: application/json

    Example Usage
     ```sh
    curl -X GET https://stacker2x.onrender.com/api/classify-numbers?numbers=371

    Example response:
     ```sh
            {
            "number": 371,
            "is_prime": false,
            "is_perfect": false,
            "properties": ["armstrong", "odd"],
            "digit_sum": 11,  // sum of its digits
            "fun_fac t": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
        }
    
    Example (Bad Requests)
    ```sh
        curl -X GET https://stacker2x.onrender.com/api/classify-numbers?
        curl -X GET https://stacker2x.onrender.com/api/classify-numbers?numbers=alphabet
        curl -X GET https://stacker2x.onrender.com/api/classify-numbers?numbers

    Example (Bad response)
    ```sh
        {
            "number": "alphabet",
            "error": true
        }


## Hire a Django Developer
Looking for skilled Django and Python developers? Check out: https://hng.tech/hire/python-developers
