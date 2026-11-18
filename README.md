# Customer Portal API

Backend service for the customer portal: account authentication, user
profiles, and billing/invoicing. Built with FastAPI and a relational
database behind SQLAlchemy.

## Running locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Project layout

```
app/
  main.py              FastAPI app and router registration
  config.py            Environment-based settings
  db.py                Database session helper
  models.py             Domain data models
  auth/                Authentication and session handling
  users/               User profile endpoints
  billing/             Invoices and billing endpoints
  notifications/       Outbound notification delivery
db_scripts/
  schema.sql           Table definitions
```
