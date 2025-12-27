from shared.a2a_protocol import A2AMessage  # Message format between agents
from datetime import datetime, timedelta   # For time calculation

class SchedulingAgent:

    def schedule_delivery(self, message: A2AMessage):
        order_id = message.payload["order_id"]          # Get order ID
        delivery_time = datetime.now() + timedelta(minutes=45)  # Add 45 minutes

        return {
            "order_id": order_id,
            "delivery_time": delivery_time.strftime("%Y-%m-%d %H:%M")  # Format time
        }


if __name__ == "__main__":
    msg = A2AMessage(
        sender="OrderingAgent",
        receiver="SchedulingAgent",
        payload={"order_id": "1234"}
    )

    agent = SchedulingAgent()
    print(agent.schedule_delivery(msg))  # Schedule and print delivery time

