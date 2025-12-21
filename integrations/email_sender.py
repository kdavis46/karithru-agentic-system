def send_confirmation(order):
    print(f"Confirmation sent for order {order.order_id}")

def send_escalation(order, reason):
    print(f"Order {order.order_id} escalated: {reason}")
