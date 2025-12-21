from models import Order, OrderItem
from decision_engine import evaluate_order


def make_order(total_value=10000, sku="SKU-123", qty=1):
    return Order(
        order_id="TEST-001",
        customer_email="test@example.com",
        items=[OrderItem(sku, qty)],
        total_value=total_value,
        raw_email_id="EMAIL-TEST"
    )


def make_customer(active=True, avg_order_value=10000):
    return {
        "active": active,
        "avg_order_value": avg_order_value
    }


def make_inventory(available=True):
    if available:
        return {"SKU-123": 100}
    return {"SKU-123": 0}


def test_happy_path_order_approved():
    order = make_order()
    customer = make_customer()
    inventory = make_inventory()

    decision = evaluate_order(order, customer, inventory)

    assert decision == "APPROVE"


def test_customer_invalid_escalation():
    order = make_order()
    customer = make_customer(active=False)
    inventory = make_inventory()

    decision = evaluate_order(order, customer, inventory)

    assert decision == "ESCALATE_CUSTOMER"


def test_inventory_unavailable_escalation():
    order = make_order()
    customer = make_customer()
    inventory = make_inventory(available=False)

    decision = evaluate_order(order, customer, inventory)

    assert decision == "ESCALATE_INVENTORY"


def test_high_value_order_escalation():
    order = make_order(total_value=300000)
    customer = make_customer(avg_order_value=20000)
    inventory = make_inventory()

    decision = evaluate_order(order, customer, inventory)

    assert decision == "ESCALATE_RISK"


def test_anomalous_order_value_escalation():
    order = make_order(total_value=50000)
    customer = make_customer(avg_order_value=10000)
    inventory = make_inventory()

    decision = evaluate_order(order, customer, inventory)

    assert decision == "ESCALATE_RISK"
