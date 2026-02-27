from src.core.events import EventBus
from src.core.audit_logger import AuditLogger

def test_eventbus_publish_subscribe():
    bus = EventBus()
    called = {"flag": False}

    def handler(data):
        called["flag"] = True
        assert data == "test"

    bus.subscribe("TestEvent", handler)
    bus.publish("TestEvent", "test")
    assert called["flag"]

def test_audit_logger(event_bus):
    logger = AuditLogger(event_bus)
    event_bus.publish("EntryAdded", {"id": 1})
    assert len(logger.logs) > 0
    assert logger.logs[-1]["action"] == "EntryAdded"
