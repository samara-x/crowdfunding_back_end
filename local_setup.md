## Local Setup Instructions

1. Create & activate virtual environment:
   - python -m venv venv
   - source venv/bin/activate   # Linux/Mac
   - venv\Scripts\activate      # Windows
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file (e.g. in project root) with at least:
   - `DJANGO_SECRET_KEY` – your secret key
   - `DJANGO_DEBUG` – set to `False` for production
4. From the `crowdfunding` directory (or project root, depending on your `manage.py` location): run `python manage.py migrate`
5. Start the server: `python manage.py runserver` (default: `http://localhost:8000/`)

## API overview

All endpoints are relative to the server root (e.g. `http://localhost:8000/`). Request and response bodies are JSON. Use header `Content-Type: application/json` for POST/PUT.

### Authentication

Protected endpoints use **Token authentication**. Include the header:

```
Authorization: Token <your-token>
```

Obtain a token by posting username and password to `POST /api-token-auth/` (see below).