# Sweet Dreams Bakery

A beautiful bakery website with a simple FastAPI backend for menu management.

## Frontend

The frontend is a static HTML website showcasing the bakery's offerings.

## Backend

A simple FastAPI application that serves menu data.

### Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the backend:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### API Endpoints

- `GET /` - Welcome message
- `GET /menu` - Get all menu items
- `GET /menu/{item_id}` - Get a specific menu item by ID
- `GET /menu/category/{category}` - Get menu items by category (bread, pastry, dessert)

### Interactive API Documentation

Once running, visit `http://localhost:8000/docs` for interactive API documentation powered by Swagger UI.

## Project Structure

```
├── index.html          # Frontend website
├── styles.css          # Frontend styles
├── script.js           # Frontend JavaScript
├── main.py             # FastAPI backend
├── requirements.txt    # Python dependencies
└── README.md          # This file
```