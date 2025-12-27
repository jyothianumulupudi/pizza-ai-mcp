# Import FastAPI framework to create APIs
from fastapi import FastAPI

# Import uuid module to generate unique order IDs
import uuid

# Create an instance of FastAPI application
app = FastAPI()


# Dictionary defining base prices for Medium-sized pizzas
# These act as the reference price for calculations
BASE_PRICES = {
    "Margherita": 299,        
    "Farmhouse": 399,         
    "Pepperoni": 399,         
    "Cheese n Corn": 309,     
    "Paneer Makhani": 459
}

# Dictionary defining price multipliers based on pizza size
# Final price = base price × size multiplier
SIZE_MULTIPLIER = {
    "Small": 0.5,     
    "Medium": 1.0,   
    "Large": 1.5
}

# Dictionary to store all placed orders
# Key   → order_id
# Value → order details
ORDERS = {}

# Root endpoint to check if the server is running
@app.get("/")
def root():
    # Return a welcome message
    return {"message": "🍕 Pizza MCP Server is running"}

# Endpoint to fetch the pizza menu
@app.get("/menu")
def get_menu():
    # Return list of pizzas with their base prices
    return {
        "menu": [
            {"name": name, "price": price}  # Each pizza name and price
            for name, price in BASE_PRICES.items()
        ]
    }

# Endpoint to place a new pizza order
@app.post("/order")
def place_order(order: dict):
    # Extract pizza name from request body
    pizza = order["pizza"]

    # Extract pizza size from request body
    size = order["size"]

    # Get base price of selected pizza
    base_price = BASE_PRICES[pizza]

    # Calculate final price using size multiplier
    final_price = int(base_price * SIZE_MULTIPLIER[size])

    # Generate a unique order ID using UUID
    order_id = str(uuid.uuid4())

    # Store order details in ORDERS dictionary
    ORDERS[order_id] = {
        "pizza": pizza,           
        "size": size,
        "price": final_price,     
        "status": "Preparing",    
        "eta": "30 minutes"       
    }

    # Return order confirmation response
    return {
        "order_id": order_id,
        "pizza": pizza,
        "size": size,
        "price": final_price,
        "status": "Preparing",
        "eta": "30 minutes"
    }

# Endpoint to track an existing order using order ID
@app.get("/order/{order_id}")
def track_order(order_id: str):
    # Fetch order details if order exists
    # If not found, return error message
    return ORDERS.get(order_id, {"error": "Order not found"})
