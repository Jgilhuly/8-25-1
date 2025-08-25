from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel

app = FastAPI(title="Sweet Dreams Bakery API", version="1.0.0")

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Menu item model
class MenuItem(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image_url: str
    category: str

# Sample menu data
menu_items = [
    MenuItem(
        id=1,
        name="Artisan Sourdough",
        description="Our famous 24-hour fermented sourdough with a perfect crust and tangy flavor.",
        price=6.50,
        image_url="https://images.unsplash.com/photo-1509440159596-0249088772ff?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80",
        category="bread"
    ),
    MenuItem(
        id=2,
        name="Butter Croissants",
        description="Flaky, buttery layers that melt in your mouth. Perfect with coffee or tea.",
        price=4.25,
        image_url="https://images.unsplash.com/photo-1555507036-ab1f4038808a?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80",
        category="pastry"
    ),
    MenuItem(
        id=3,
        name="Chocolate Dream Cake",
        description="Rich chocolate layers with ganache frosting. A chocolate lover's paradise.",
        price=8.99,
        image_url="https://images.unsplash.com/photo-1565958011703-44f9829ba187?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80",
        category="dessert"
    ),
    MenuItem(
        id=4,
        name="Cinnamon Rolls",
        description="Soft, fluffy rolls with cinnamon sugar and cream cheese frosting.",
        price=5.50,
        image_url="https://images.unsplash.com/photo-1608198093002-ad4e505484ba?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80",
        category="pastry"
    )
]

@app.get("/")
async def root():
    return {"message": "Welcome to Sweet Dreams Bakery API!"}

@app.get("/menu", response_model=List[MenuItem])
async def get_menu():
    """Get all menu items"""
    return menu_items

@app.get("/menu/{item_id}", response_model=MenuItem)
async def get_menu_item(item_id: int):
    """Get a specific menu item by ID"""
    for item in menu_items:
        if item.id == item_id:
            return item
    return {"error": "Menu item not found"}

@app.get("/menu/category/{category}")
async def get_menu_by_category(category: str):
    """Get menu items by category"""
    filtered_items = [item for item in menu_items if item.category.lower() == category.lower()]
    return filtered_items

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
