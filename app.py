from models import Order, OrderItem
from decision_engine import evaluate_order
from monitoring.audit import log_event
from integrations.salesforce import get_customer
from integrations.inventory import check_inventory
from integrations.email_sender import send_confirmation, send_escalation
from metrics import Metrics
from config import MAX_PROCESSING_SECONDS


def process_order(order: Order):
    metrics = Metrics()
    metrics.start()

    customer = get_customer(order.customer_email)
    inventory = check_inventory()

    decision = evaluate_order(order, customer, inventory)
    log_event("DECISION", {"order": order.order_id, "decision": decision})

    if decision == "APPROVE":
        send_confirmation(order)
        log_event("ORDER_APPROVED", {"order": order.order_id})
    else:
        send_escalation(order, decision)
        log_event("ORDER_ESCALATED", {"order": order.order_id, "reason": decision})

    metrics.stop()
    elapsed = metrics.elapsed_seconds

    log_event("PROCESS_TIME", {"order": order.order_id, "seconds": elapsed})

    if elapsed > MAX_PROCESSING_SECONDS:
        log_event(
            "SLO_BREACH",
            {
                "order": order.order_id,
                "elapsed_seconds": elapsed,
                "slo_seconds": MAX_PROCESSING_SECONDS
            }
        )


if __name__ == "__main__":
    order = Order(
        order_id="ORD-001",
        customer_email="customer@example.com",
        items=[OrderItem("SKU-123", 2)],
        total_value=18000,
        raw_email_id="EMAIL-ABC"
    )

    process_order(order)
