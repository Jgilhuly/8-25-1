import pytest
from fastapi.testclient import TestClient
from main import app, menu_items

# Create test client
client = TestClient(app)


class TestRootEndpoint:
    """Test the root endpoint"""
    
    def test_root_endpoint(self):
        """Test GET / returns welcome message"""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to Sweet Dreams Bakery API!"}


class TestMenuEndpoints:
    """Test menu-related endpoints"""
    
    def test_get_all_menu_items(self):
        """Test GET /menu returns all menu items"""
        response = client.get("/menu")
        assert response.status_code == 200
        data = response.json()
        
        # Should return a list of menu items
        assert isinstance(data, list)
        assert len(data) == len(menu_items)
        
        # Verify first item structure
        assert "id" in data[0]
        assert "name" in data[0]
        assert "description" in data[0]
        assert "price" in data[0]
        assert "image_url" in data[0]
        assert "category" in data[0]
    
    def test_get_specific_menu_item_valid_id(self):
        """Test GET /menu/{id} with valid ID"""
        # Test with first menu item
        item_id = menu_items[0].id
        response = client.get(f"/menu/{item_id}")
        assert response.status_code == 200
        
        data = response.json()
        assert data["id"] == item_id
        assert data["name"] == menu_items[0].name
        assert data["description"] == menu_items[0].description
        assert data["price"] == menu_items[0].price
        assert data["category"] == menu_items[0].category
    
    def test_get_specific_menu_item_invalid_id(self):
        """Test GET /menu/{id} with non-existent ID"""
        invalid_id = 999
        response = client.get(f"/menu/{invalid_id}")
        assert response.status_code == 404  # Should return 404 for not found
        data = response.json()
        assert data["detail"] == "Menu item not found"
    
    def test_get_menu_by_category_valid(self):
        """Test GET /menu/category/{category} with valid category"""
        # Test with 'bread' category
        response = client.get("/menu/category/bread")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        
        # All items should be bread category
        for item in data:
            assert item["category"] == "bread"
        
        # Should contain the sourdough item
        bread_items = [item for item in data if item["name"] == "Artisan Sourdough"]
        assert len(bread_items) == 1
    
    def test_get_menu_by_category_case_insensitive(self):
        """Test GET /menu/category/{category} is case insensitive"""
        # Test with uppercase category
        response = client.get("/menu/category/PASTRY")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        
        # All items should be pastry category
        for item in data:
            assert item["category"].lower() == "pastry"
    
    def test_get_menu_by_category_empty_result(self):
        """Test GET /menu/category/{category} with non-existent category"""
        response = client.get("/menu/category/nonexistent")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 0  # Should return empty list
    
    def test_get_menu_by_category_multiple_items(self):
        """Test GET /menu/category/{category} with category that has multiple items"""
        response = client.get("/menu/category/pastry")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 2  # Should have multiple pastry items
        
        # Verify all are pastry items
        for item in data:
            assert item["category"] == "pastry"


class TestMenuItemStructure:
    """Test menu item data structure and validation"""
    
    def test_menu_item_data_types(self):
        """Test that menu items have correct data types"""
        response = client.get("/menu")
        assert response.status_code == 200
        
        data = response.json()
        for item in data:
            assert isinstance(item["id"], int)
            assert isinstance(item["name"], str)
            assert isinstance(item["description"], str)
            assert isinstance(item["price"], (int, float))
            assert isinstance(item["image_url"], str)
            assert isinstance(item["category"], str)
    
    def test_menu_item_required_fields(self):
        """Test that all menu items have required fields"""
        response = client.get("/menu")
        assert response.status_code == 200
        
        data = response.json()
        required_fields = ["id", "name", "description", "price", "image_url", "category"]
        
        for item in data:
            for field in required_fields:
                assert field in item
                assert item[field] is not None
                assert item[field] != ""  # Ensure string fields are not empty
    
    def test_menu_item_unique_ids(self):
        """Test that all menu items have unique IDs"""
        response = client.get("/menu")
        assert response.status_code == 200
        
        data = response.json()
        ids = [item["id"] for item in data]
        assert len(ids) == len(set(ids))  # No duplicate IDs


class TestAPIResponseHeaders:
    """Test API response headers and CORS"""
    
    def test_cors_headers_present(self):
        """Test that CORS headers are present in responses"""
        response = client.get("/menu")
        assert response.status_code == 200
        
        # FastAPI's TestClient doesn't automatically include CORS headers
        # but we can verify the middleware is configured by checking the app
        from main import app
        middlewares = [middleware.cls.__name__ for middleware in app.user_middleware]
        assert "CORSMiddleware" in middlewares


class TestEdgeCases:
    """Test edge cases and error conditions"""
    
    def test_negative_menu_item_id(self):
        """Test GET /menu/{id} with negative ID"""
        response = client.get("/menu/-1")
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Menu item not found"
    
    def test_zero_menu_item_id(self):
        """Test GET /menu/{id} with zero ID"""
        response = client.get("/menu/0")
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Menu item not found"
    
    def test_string_menu_item_id(self):
        """Test GET /menu/{id} with string ID (should return 422)"""
        response = client.get("/menu/abc")
        assert response.status_code == 422  # Validation error
    
    def test_empty_category_string(self):
        """Test GET /menu/category/{category} with empty category"""
        response = client.get("/menu/category/")
        # This should return 422 as the route doesn't match (empty path parameter)
        assert response.status_code == 422


# Performance and load testing can be added here
class TestPerformance:
    """Basic performance tests"""
    
    def test_menu_endpoint_response_time(self):
        """Test that menu endpoint responds quickly"""
        import time
        
        start_time = time.time()
        response = client.get("/menu")
        end_time = time.time()
        
        assert response.status_code == 200
        assert (end_time - start_time) < 1.0  # Should respond within 1 second


if __name__ == "__main__":
    # Run tests when script is executed directly
    pytest.main([__file__, "-v"])