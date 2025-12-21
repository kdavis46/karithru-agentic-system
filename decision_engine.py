from config import HIGH_VALUE_THRESHOLD, ANOMALY_MULTIPLIER

def evaluate_order(order, customer, inventory_snapshot):
    decisions = {}

    decisions["customer_valid"] = customer["active"]
    decisions["inventory_available"] = all(
        inventory_snapshot.get(item.sku, 0) >= item.quantity
        for item in order.items
    )

    decisions["high_value"] = order.total_value >= HIGH_VALUE_THRESHOLD
    decisions["anomaly"] = order.total_value > (
        customer["avg_order_value"] * ANOMALY_MULTIPLIER
    )

    if not decisions["customer_valid"]:
        return "ESCALATE_CUSTOMER"

    if not decisions["inventory_available"]:
        return "ESCALATE_INVENTORY"

    if decisions["high_value"] or decisions["anomaly"]:
        return "ESCALATE_RISK"

    return "APPROVE"
