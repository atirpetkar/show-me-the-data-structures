class Node(object):
    """Node class for use in the doubly linked list
    """

    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CacheUsageQueue(object):
    """CacheUsageQueue
    Implemented with a doubly linked list for storing the cache usage
    The head of the queue is the most recently hit or newly inserted key
    The tail of the queue is the least recently used (LRU) key
    """

    def __init__(self):
        self.head = None
        self.tail = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        pass


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(3)       # return -1
