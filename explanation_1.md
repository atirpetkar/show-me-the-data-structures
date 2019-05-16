# Problem 2 - LRU Cache - Explanation

## Data Structure Design
I used 2 data structures to implement a LRU cache:
+ A queue backed by a doubly linked list was used to keep tracking of the cache keys that are being accessed.
  - The head of the queue is the least recently used key
  - The tail of the queue is the newly added or recently visited item
  - Every time a new entry was added, a node will be enqueued
  - Every time a node was visited, the node will be moved to the end of the queue
  - Every an item need to remove, the dequeued node will be removed as it is the LRU one
+ A Python dict was used to store the cache items. For each item, there will be key/value pairs. The key is the key of the cache, while the value is a tuple. The first position is the value, while the second position is the node reference to the corresponding node in the queue.
  - When a new item was set, it will call the enqueue function of the above queue, and a reference of the node will be returned. Then it will be saved to the dict with the key value
  - When an item was visited, the node reference will be passed to the queue to move to queue's end. So it's the most recently used one
  - When an item need to be removed, the dequeue function of the cache queue will be called. The key returned will be removed from the dict of the cache

## Run time complexity
The run time complexity for accessing a Python dict is of O(1)
The run time complexity for enqueue, dequeue, and move node to end of queue function are all of O(1)

As a result, the run time complexity of this implementation is O(1)
