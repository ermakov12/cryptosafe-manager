# tests/test_events.py
import pytest
from src.core.events import EventBus
from src.core.audit_logger import AuditLogger

def test_event_publish_subscribe(event_bus):
    received = []

    def handler(data):
        received.append(data)

    event_bus.subscribe("TestEvent", handler)
    event_bus.publish("TestEvent", {"foo": "bar"})
    assert received[0] == {"foo": "bar"}

def test_audit_logger(event_bus):
    logger = AuditLogger(event_bus)
    event_bus.publish("EntryAdded", {"id": 1})
    assert len(logger.logs) > 0
