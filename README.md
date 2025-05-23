# Secure Python Login System

## Description
This project is a command-line login system implemented in Python, designed as a learning exercise to understand and practice:
- SQLAlchemy ORM for database operations
- Database management with Python
- MVC (Model-View-Controller) architectural pattern
- Secure user authentication with password encryption
- Password hashing and salting for enhanced security

## Project Structure
```
login/
├── __init__.py
├── run.py                 # Main entry point of the application
├── controllers/          
│   ├── __init__.py
│   ├── login.py          # Handles login logic
│   └── register.py       # Handles user registration
├── models/
│   ├── database.py       # Database configuration and session management
│   └── user.py          # User model and database operations
└── views/
    ├── __init__.py
    └── main_view.py     # User interface and input handling
```

## Features
- Secure user registration with password hashing
- Encrypted user authentication
- Secure password input (hidden input)
- Password salting and hashing using sha256
- Database persistence using SQLAlchemy
- MVC architecture implementation
- Protection against common security vulnerabilities

## Technologies Used
- Python
- SQLAlchemy (ORM)
- PostgreSQL Database
- getpass (for secure password input)
- Hashlib & sha256 (for password hashing)

## Architecture
The project follows the MVC (Model-View-Controller) pattern:
- **Models**: Handle data logic and database operations (User model)
- **Views**: Handle user interface and data presentation
- **Controllers**: Handle business logic and coordinate between Models and Views

## Getting Started

### Prerequisites
- Python 3.x
- SQLAlchemy
- PostgreSQL
- hashlib (sha256)

### Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install sqlalchemy
```

### Running the Application
Navigate to the project directory and run:
```bash
python run.py
```

## Project Components

### Models
- `database.py`: Manages database connection and session creation with secure connection handling
- `user.py`: Defines User model with encrypted data fields and secure database operations

### Controllers
- `login.py`: Handles secure user authentication with encrypted password verification
- `register.py`: Manages user registration with password hashing and data encryption

### Views
- `main_view.py`: Provides user interface with secure input handling and sanitization

### Database Security
1. **Data Protection**
   - Encrypted sensitive fields
   - Parameterized queries to prevent SQL injection
   - Secure connection handling

2. **Access Control**
   - Principle of least privilege
   - Prepared statements for all database operations
   - Input validation and sanitization

## Learning Outcomes
This project demonstrates:
1. Implementation of MVC pattern in Python
2. Database operations using SQLAlchemy ORM
3. Secure user authentication principles
4. Cryptographic implementations in Python
5. Password hashing and salting techniques
6. Security best practices in CLI applications
7. Clean code organization and structure
8. Defensive programming techniques

## Security Features and Best Practices
- Separation of concerns (MVC pattern)
- Password hashing using SHA256
- Protection against rainbow table attacks
- Secure password input using getpass
- No plain-text password storage
- Proper exception handling for database operations
- Clean project structure
- Modular code organization
- Security-first approach to user data
