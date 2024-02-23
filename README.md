# NeoFi Python Backend

This repository contains the code for the NeoFi Python backend, developed by Rajnish Singh Thakur as part of the NeoFi assessment.

## About the App

This is a Django web application that provides [brief description of your app].

## Dependencies

- Python 3.9.0
- Django 4.2.2

## Installation

1. **Clone the repository to your local machine:**
    ```bash
    git clone https://github.com/RajnishProgrammer/neofi_python_backend.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd neofi_python_backend
    ```

3. **Install the required dependencies using pip:**
    ```bash
    pip install -r requirements.txt
    ```

## Setup

1. **Configure the database settings in `settings.py` according to your environment.**

2. **Apply migrations to create database tables:**
    ```bash
    python manage.py migrate
    ```

3. **(Optional) Create a superuser for accessing the Django admin interface:**
    ```bash
    python manage.py createsuperuser
    ```
    - Then enter username, email, and password

## Running the Project

To run the Django development server, use the following command:

```bash
python manage.py runserver
```

## For automated testing
- In project directory run:
``` python manage.py test ```

## Testing APIs

- Navigate to the `tests` folder in the command prompt.
- Run the `signup_api.py` file to register a user: `python signup_api.py`.
- Next, run the `login_api.py` file to obtain the authentication token for the registered user: `python login_api.py`. Save this token for future operations.
- To test other APIs, use the obtained authentication token and update the data (content) and headers of the request accordingly.
- Follow the provided test format and adjust the request parameters as needed.

## Contact Me
[Email:] rajnishsinghthakur107@gmail.com
