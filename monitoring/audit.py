import json
from datetime import datetime

def log_event(event_type: str, payload: dict):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "payload": payload
    }
    print(json.dumps(record))
