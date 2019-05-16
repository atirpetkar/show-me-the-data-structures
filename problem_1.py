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
    The head of the queue is the least recently used (LRU) key
    The tail of the queue is the most recently hit or newly inserted key
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, key):
        """
        Add a new cache key into the queue
        :param key: the key in the cache
        :return: the associated node in the queue
        """

        new_node = Node(key)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        return new_node

    def move_to_end(self, node):
        """
        Move a node from it's current position to end of queue (e.g. after a cache hit)
        :param node: the node to move
        :return: None
        """

        # No need to move if node already at queue end
        if node is self.tail:
            return

        # If the node is at the head of the queue
        if node is self.head:
            self.head.next.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail
            temp = self.head
            self.head = self.head.next
            self.tail = self.tail.next
            temp.next = None
            return

        # Node is in between the head and tail
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail
        node.next = None
        self.tail = node

    def dequeue(self):
        """
        Dequeue the node from head of queue, which is the LRU cache key
        :return: the key which was being dequeue
        """

        node = self.head

        self.head = self.head.next
        self.head.prev = None
        node.next = None

        return node.value


class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables

        # A dict structure for storing the cache key and value.
        # The value is a tuple. The first position is the value,
        # while the second position is the reference to the node in the cache queue
        self.cache_dict = {}

        # Initialize the queue to store the LRU cache entru
        self.cache_usage_queue = CacheUsageQueue()

        # Store the capacity of the cache
        self.capacity = capacity

        # Store the size of the entries
        self.size = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        # Check whether the key in cache
        value = -1
        if key in self.cache_dict:
            value = self.cache_dict[key][0]
            queue_node = self.cache_dict[key][1]

            # Move the node to the end of queue for every cache hit
            self.cache_usage_queue.move_to_end(queue_node)

        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        # If current size equals capacity, dequeue the LRU entry
        if self.size == self.capacity:
            dequeued_key = self.cache_usage_queue.dequeue()
            del self.cache_dict[dequeued_key]
            self.size -= 1

        # Add the key value into cache and enqueue to the usage queue
        cache_node = self.cache_usage_queue.enqueue(key)
        self.cache_dict[key] = (value, cache_node)
        self.size += 1


# Test case 1 - set cache within capacity and try get with exist and non-exist key
print("Initialize an empty cache of capacity 5")
our_cache = LRU_Cache(5)
print("Put key:value 1:1 into cache")
our_cache.set(1, 1)
print("Put key:value 2:2 into cache")
our_cache.set(2, 2)
cache_value = our_cache.get(1)       # returns 1
print(cache_value)
# Should print 1
cache_value = our_cache.get(2)       # returns 2
print(cache_value)
# Should print 2
cache_value = our_cache.get(3)       # return -1
print(cache_value)
# Should print -1


# Test case 2 - set cache that exceeded capacity and try get with exist and non-exist key
our_cache = LRU_Cache(5)
# Add cache keys to the capacity
print("Add cache keys to the capacity")
print("Put key:value 1:1 into cache")
our_cache.set(1, 1)
print("Put key:value 2:2 into cache")
our_cache.set(2, 2)
print("Put key:value 3:3 into cache")
our_cache.set(3, 3)
print("Put key:value 4:4 into cache")
our_cache.set(4, 4)
print("Put key:value 5:5 into cache")
our_cache.set(5, 5)
cache_value = our_cache.get(1)       # returns 1
print(cache_value)
# Should print 1
cache_value = our_cache.get(2)       # returns 2
print(cache_value)
# Should print 2
cache_value = our_cache.get(3)       # return 3
print(cache_value)
# Should print 3
cache_value = our_cache.get(5)       # return 5
print(cache_value)
# Should print 5
print("Add entry to remove the LRU entry from cache")
print("Put key:value 6:6 into cache")
our_cache.set(6, 6)
print("As key 4 was not accessed before, it should be removed from cache")
cache_value = our_cache.get(4)       # return -1
print(cache_value)
# Should print -1
cache_value = our_cache.get(6)       # return 6
print(cache_value)
# Should print 6


# Test case 3 - empty cache should return -1 for all keys
print("Initialize an empty cache of capacity 5")
our_cache = LRU_Cache(5)
cache_value = our_cache.get(1)       # returns -1
print(cache_value)
# Should print -1
cache_value = our_cache.get(2)       # returns -1
print(cache_value)
# Should print -1
