# BookReviewApi
> Backend service to power an open community for reviewing books

## Table of Contents
1. [About the Project](#-about-the-project)
2. [Tech Stack](#-tech-stack)
3. [Features](#-features)
4. [Architecture](#-architecture)
5. [Folder Structure](#-folder-structure)
6. [API Documentation](#-api-documentation)
7. [Authentication](#-authentication)
8. [Environmental Variables](#-environmental-variables)
9. [Installation](#-installation)
10. [Running the Project](#-running-the-project)
11. [Deployment](#-deployment)
12. [Contributing](#-contributing)
13. [Author](#-author)


## 📘 About the Project
BookReviewApi is a backend API service for Book Log app where readers can drop a rating and comment about any book they are reading or have read. They are free to drop their opinion and also see that of others about their favourite books.

## 🧰 Tech Stack
- Backend: Flask (Python), Flask-RESTful
- Database: MySQL
- Authentication: Flask-JWT-Extended
- ORM: SQLAlchemy
- Deployment: pythonanywhere
- Documentation: Postman

## 🌟 Features
- Add and retrieve book reviews
- Submit ratings (e.g., 1-5 stars)
- Comment on books
- User registration and authentication
- View community opinion
- Book rating aggregation (coming soon)
- Filter and search books by titile and author (coming soon)
- Post a book with a description

## 🧱 Architecture
The **BookReviewAPI** is built using `Flask-RESTful`, with a modular organization of API endpoints into separate files for scalability and clarity.   
Key architectural components include:
- `Flask-RESTful` for building RESTful APIs using resource classes.
- Modular API structure:
  - Each API resource (e.g., `BooksResource`, `ReviewsResource`, `Login`) is defined in a separate Python file.
  - Resources are registered centrally in `api/__init__.py ` using `api.add_resource()`.
- SQLAlchemy ORM models for Users, Books, Genres and Reviews.
- JWT-based authentication
- RESTful API design

## 📂 Folder Structure
```bash
.
├── api
│   ├── book_api.py
│   ├── __init__.py
│   ├── review_api.py
│   ├── search_api.py
│   ├── status.py
│   └── user_api.py
├── app.py
├── dummy_data.py
├── __init__.py
├── models
│   ├── base.py
│   ├── books.py
│   ├── engine
│   │   ├── db_storage.py
│   │   └── __init__.py
│   ├── genres.py
│   ├── __init__.py
│   ├── reviews.py
│   └── users.py
├── README.md
└── requirements.txt
```

## 📡 API Documentation
- Postman Collection: [link](#) (coming soon)

Example Endpoints:
```bash
GET /api/books  # Get a list of all books
GET /api/book/<int:book_id>/review  # Get all reviews for a book
POST /api/book/<int:id> # Post a book
```

## 🔐 Authentication
- JWT Authentication
- Register/Login to receive a token
- Include in headers: `Authorization: Bearer <your_token>`

## ⚙️ Environmental Variables
```env
APP_KEY='<app secret key>'
SQLALCHEMY_DATABASE_URI=mysql+pymysql://user:password@host:port/dbname
```
Store in a `.env` file.

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/chisomdaniel/BookReviewApi.git
cd BookReviewApi

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
vi .env

# Start the server
./app.py

```

## ▶️ Running the Project
```
./app.py
```
Access the API at: `http://127.0.0.1:5000/`

## 🚀 Deployment
- Platform: Render / Heroku / AWS / Railway
- Configure `Procfile` and `requirements.txt`
- Add environment variables on your hosting platform

## 🤝 Contributing
1. Fork the repository
2. Create a new feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push to your fork (`git push origin feature/your-feature`)
5. Create a pull request

## 👤 Author
**Chukwusom Daniel Chinweze**  
Email: chinwezechisom@gmail.com  
GitHub: [@chisomdaniel](github.com/chisomdaniel)  
Linkedin: [Chisom Chinweze](linkedin.com/in/chisom-chinweze)

[Back to top](#bookreviewapi)
