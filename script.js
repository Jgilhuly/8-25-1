// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Fetch menu data from the backend API
    fetchMenuData();
});

async function fetchMenuData() {
    try {
        const response = await fetch('http://localhost:8000/menu');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const menuItems = await response.json();
        displayMenu(menuItems);
    } catch (error) {
        console.error('Error fetching menu data:', error);
        // Fallback to static content if API is not available
        displayFallbackMessage();
    }
}

function displayMenu(menuItems) {
    const menuGrid = document.querySelector('.menu-grid');
    if (!menuGrid) return;

    // Clear existing content
    menuGrid.innerHTML = '';

    // Create menu items dynamically
    menuItems.forEach(item => {
        const menuItem = document.createElement('div');
        menuItem.className = 'menu-item';
        menuItem.innerHTML = `
            <img src="${item.image_url}" alt="${item.name}">
            <div class="menu-item-content">
                <h3>${item.name}</h3>
                <p>${item.description}</p>
                <p class="price">$${item.price.toFixed(2)}</p>
            </div>
        `;
        menuGrid.appendChild(menuItem);
    });
}

function displayFallbackMessage() {
    const menuGrid = document.querySelector('.menu-grid');
    if (!menuGrid) return;

    menuGrid.innerHTML = `
        <div class="fallback-message">
            <p>🍞 Our delicious menu is currently being prepared!</p>
            <p>Please check back soon or visit us in person to see our fresh offerings.</p>
        </div>
    `;
}

// Add loading state
function showLoading() {
    const menuGrid = document.querySelector('.menu-grid');
    if (!menuGrid) return;

    menuGrid.innerHTML = `
        <div class="loading-message">
            <p>🥖 Loading our fresh menu...</p>
        </div>
    `;
}
