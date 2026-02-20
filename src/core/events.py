from collections import defaultdict

class EventBus:

    def __init__(self):
        self._subscribers = defaultdict(list)

    def subscribe(self, event_type, handler):
        self._subscribers[event_type].append(handler)

    def publish(self, event_type, data=None):
        for handler in self._subscribers[event_type]:
            handler(data)
