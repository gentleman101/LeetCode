from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()  # Maintains order of keys based on usage

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed key to the end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move key to the end
            self.cache.move_to_end(key)
        else:
            # If the cache is full, remove the least recently used item
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)  # Removes the first (oldest) item
        self.cache[key] = value
