import pytest
from src.core.audit_logger import AuditLogger

def test_audit_logger(event_bus):
    logger = AuditLogger(event_bus)
    event_bus.publish("EntryAdded", {"id": 1})
    assert len(logger.logs) > 0
