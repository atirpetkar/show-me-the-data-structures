class HashTable(object):
    """
    Hash table to calculate the hash value and store it in an array for searching
    """
    def __init__(self, initial_size=100):
        self.table = [None] * initial_size
        self.p = 31

    def store(self, value):
        bucket_index = self.calculate_hash_value(value)

        self.table[bucket_index] = value

    def lookup(self, value):
        """
        Lookup a value in hash table.
        :param value: value
        :return: value if found. If not found, return None
        """
        bucket_index = self.calculate_hash_value(value)

        return self.table[bucket_index]

    def calculate_hash_value(self, value):
        """
        Calculate the hash value of a provided value
        :param value: the value for calculating the hash
        :return: the hash value
        """
        num_buckets = len(self.table)

        # Convert the provided value into string
        string_value = str(value)

        # Calculate the hash value
        hash_value = 0
        current_coefficient = 1

        for char in string_value:
            hash_value += ord(char) * current_coefficient
            hash_value = hash_value % num_buckets
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets

        return hash_value % num_buckets


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here

    # Initialize a hash table for storing list values
    hash_table = HashTable()

    # Initialize a linked list to store the union result
    union_list = LinkedList()

    # Traverse through list_1, add all elements to hash table and result list
    # Nodes in linked list with same value will only add once to the result list
    cur_node = llist_1.head
    while cur_node:
        value = cur_node.value
        if hash_table.lookup(value) is None:
            hash_table.store(value)
            union_list.append(value)
        cur_node = cur_node.next

    # Traverse through list_2, check hash table, if not exist, then add to hash table and result list
    cur_node = llist_2.head
    while cur_node:
        value = cur_node.value
        if hash_table.lookup(value) is None:
            hash_table.store(value)
            union_list.append(value)
        cur_node = cur_node.next

    return union_list


def intersection(llist_1, llist_2):
    # Your Solution Here

    # Initialize a hash table for storing list values
    hash_table = HashTable()

    # Initialize a linked list to store the intersection result
    intersection_list = LinkedList()

    # Traverse through list_1, add all elements to hash table
    # Nodes in linked list with same value will be ignored
    cur_node = llist_1.head
    while cur_node:
        value = cur_node.value
        if hash_table.lookup(value) is None:
            hash_table.store(value)
        cur_node = cur_node.next

    # Traverse through list_2, check hash table, if exist, then add to result list
    # Store a list of values added to the list to eliminate duplicate items
    added_value_list = list()
    cur_node = llist_2.head
    while cur_node:
        value = cur_node.value
        if hash_table.lookup(value) and value not in added_value_list:
            intersection_list.append(value)
            added_value_list.append(value)
        cur_node = cur_node.next

    return intersection_list


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Input lists: [3,2,4,35,6,65,6,4,3,21], [6,32,4,9,6,1,11,21,1]")
print("Calling union")
print(union(linked_list_1,linked_list_2))
# Should print 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
print("Calling intersection")
print(intersection(linked_list_1,linked_list_2))
# Should print 6 -> 4 -> 21 ->

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Input lists: [3,2,4,35,6,65,6,4,3,23], [1,7,8,9,11,21,1]")
print("Calling union")
print (union(linked_list_3,linked_list_4))
# Should print 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print("Calling intersection")
print (intersection(linked_list_3,linked_list_4))
# Should print empty string

# Test case 3 - Both lists are empty
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
element_1 = list()
element_2 = list()

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print("Input lists: [], []")
print("Calling union")
print (union(linked_list_5,linked_list_6))
# Should print empty string
print("Calling intersection")
print (intersection(linked_list_5,linked_list_6))
# Should print empty string

# Test case 4 - One list is empty
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()
element_1 = list()
element_2 = [1, 2]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print("Input lists: [], [1, 2]")
print("Calling union")
print (union(linked_list_7,linked_list_8))
# Should print 1 -> 2 ->
print("Calling intersection")
print (intersection(linked_list_7,linked_list_8))
# Should print empty string
