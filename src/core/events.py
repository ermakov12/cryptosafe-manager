from collections import defaultdict
from typing import Callable, Dict, List, Any
from enum import Enum


class EventType(str, Enum):
    ENTRY_CREATED = "entry_created"
    ENTRY_DELETED = "entry_deleted"


class EventBus:
    def __init__(self):
        self._subscribers: Dict[EventType, List[Callable]] = defaultdict(list)

    def subscribe(self, event: EventType, handler: Callable):
        self._subscribers[event].append(handler)

    def publish(self, event: EventType, data: Any = None):
        for handler in self._subscribers[event]:
            handler(data)
