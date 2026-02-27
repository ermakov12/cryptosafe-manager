from core.events import EventBus, EventType


def test_event_publish():
    bus = EventBus()
    result = []

    def handler(data):
        result.append(data)

    bus.subscribe(EventType.ENTRY_CREATED, handler)
    bus.publish(EventType.ENTRY_CREATED, "ok")

    assert result == ["ok"]
