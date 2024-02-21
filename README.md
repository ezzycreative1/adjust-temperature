# FastAPI Image Temperature Adjustment

## Overview

This FastAPI project is designed to demonstrate image temperature adjustment functionality. It provides an endpoint for adjusting the temperature of a JPEG image and saving the adjusted image.

## Features

- **Adjust Temperature Endpoint:** Accepts a JPEG image file and a temperature adjustment value, and returns the adjusted image.

## Requirements

- Python 3.7 or higher
- FastAPI

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/fastapi-image-temperature.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

2. Open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the Swagger documentation.

3. Use the Swagger documentation to test the `/adjust-temperature` endpoint by uploading a JPEG image and providing a temperature adjustment value.

## Configuration

- CORS (Cross-Origin Resource Sharing) is enabled in this project to allow access from all domains. Modify the CORS configuration in `main.py` based on your specific needs.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
