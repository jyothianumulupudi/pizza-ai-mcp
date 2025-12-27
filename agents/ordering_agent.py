import requests  # To send HTTP requests

class OrderingAgent:

    def __init__(self, mcp_url):
        self.mcp_url = mcp_url  # MCP server URL

        # Mapping user keywords to pizza names
        self.pizza_menu = {
            "margherita": "Margherita",
            "farmhouse": "Farmhouse",
            "pepperoni": "Pepperoni",
            "cheese n corn": "Cheese n Corn",
            "cheese and corn": "Cheese n Corn",
            "paneer makhani": "Paneer Makhani"
        }

    def extract_pizza(self, user_text):
        text = user_text.lower()  # Convert text to lowercase
        for key, pizza_name in self.pizza_menu.items():
            if key in text:       # Match pizza name
                return pizza_name
        return "Margherita"       # Default pizza

    def extract_size(self, user_text):
        # Check pizza size from user text
        return "Large" if "large" in user_text.lower() else "Medium"

    def order_pizza(self, user_text):
        pizza = self.extract_pizza(user_text)  # Get pizza name
        size = self.extract_size(user_text)    # Get pizza size

        # Send order request to MCP server
        response = requests.post(
            f"{self.mcp_url}/order",
            json={"pizza": pizza, "size": size}
        )

        return response.json()  # Return server response


if __name__ == "__main__":
    agent = OrderingAgent("http://localhost:8000")  # Create agent

    # Sample user orders
    test_orders = [
        "I want a large Margherita",
        "Order pepperoni pizza",
        "Get me cheese n corn",
        "I want a large paneer makhani",
        "Farmhouse medium please"
    ]

    for order in test_orders:
        print(f"\nUser: {order}")
        print("Agent:", agent.order_pizza(order))  # Place order
