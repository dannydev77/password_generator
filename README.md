# OpenSSL Password Generator

A simple web app for generating random passwords using OpenSSL's cryptographically secure random number generator.  
Built with Python Flask backend and a Bootstrap-powered frontend.

---

## Features

- Generate passwords of customizable length  
- Choose character sets: uppercase, lowercase, numbers, symbols  
- Password strength meter  
- Copy generated password to clipboard  
- Backend uses OpenSSL for strong randomness  
- Dockerized for easy deployment  

---

## Requirements

- Python 3.11+  
- OpenSSL installed (backend dependency)  
- Docker (optional, for containerized deployment)  

---

## Setup

1. **Clone the repository**

```git clone https://github.com/dannydev77/password_generator.git```

```cd <password_generator```

2. **Install Python dependencies**

```pip install -r requirements.txt```


Run the app

```python app.py```

Open your browser at http://localhost:5000

## Docker

Build and run with Docker Compose:

```docker-compose up --build```


App will be available at http://localhost:5000.

Usage

Select desired password length and character types

Click Generate Password

View the password strength meter

Copy password with the Copy button

License

MIT License