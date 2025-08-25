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

### Testing

The project includes comprehensive unit tests for all API endpoints.

#### Running Tests

1. Make sure dependencies are installed (including test dependencies):
```bash
pip install -r requirements.txt
```

2. Run tests using the test runner script:
```bash
python3 run_tests.py
```

Or run tests directly with pytest:
```bash
python3 -m pytest test_main.py -v
```

#### Test Coverage

The test suite includes:
- ✅ Root endpoint testing
- ✅ Menu endpoints (GET /menu, GET /menu/{id}, GET /menu/category/{category})
- ✅ Data validation and structure tests
- ✅ Edge cases (invalid IDs, non-existent categories)
- ✅ Error handling (404 errors, validation errors)
- ✅ CORS middleware verification
- ✅ Basic performance testing

## Project Structure

```
├── index.html          # Frontend website
├── styles.css          # Frontend styles
├── script.js           # Frontend JavaScript
├── main.py             # FastAPI backend
├── test_main.py        # Unit tests for API endpoints
├── run_tests.py        # Test runner script
├── requirements.txt    # Python dependencies (including test dependencies)
└── README.md          # This file
```