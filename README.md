# OrvynCore

A Django REST Framework backend project with PostgreSQL integration.

## Project Setup

### Prerequisites

- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Cronos891/OrvynCore.git
cd OrvynCore
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a .env file in the project root and add your environment variables:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DB_HOST=localhost
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

5. Run migrations:

```bash
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Start the development server:

```bash
python manage.py runserver
```

## API Documentation

Once the server is running, you can access the API documentation at:

- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## Development and Production Databases

The project is configured with separate database settings for development and production environments:

### Development Database

- Name: OrvynCore
- User: postgres
- Host: localhost
- Port: 5432

### Production Database

- Name: orvyn_db
- User: orvyn_db_user
- Host: (configured via environment variable)
- Port: 5432

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Submit a pull request

## License

This project is licensed under the BSD License.
