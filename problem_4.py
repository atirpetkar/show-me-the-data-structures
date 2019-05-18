class HashTable(object):
    """
    Hash table to calculate the hash value and store it in an array for searching
    """
    def __init__(self, initial_size=100):
        self.table = [None] * initial_size
        self.p = 31
        self.size = initial_size

    def store(self, value, child_table=None):
        """
        Store a new entry in hash table
        - If child table exist (group will contains a user hash table),
        - the child table will be stored as the value
        :param value: the user/group id
        :param child_table: user_hash_table if it's a hash table for group
        :return: for user, return user_id. For group, return group's user_hash_table
        """
        bucket_index = self.calculate_hash_value(value)

        if child_table:
            self.table[bucket_index] = child_table
        else:
            self.table[bucket_index] = value

    def lookup(self, value):
        """
        Lookup a value in hash table.
        :param value: value
        :return: value if found. If not found, return None
        """
        bucket_index = self.calculate_hash_value(value)

        return self.table[bucket_index]

    def clear(self):
        # Clear all hast table entries
        self.table = [None] * self.size

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


# Initialize a hash table for groups
group_hash_table = HashTable()


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        self.user_hash_table = HashTable()

        # Store the group and it's user hash table into the group hash table
        group_hash_table.store(self.name, self.user_hash_table)

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

        # Add the user entry into the user hash table of the group hash record
        user_hash_table = group_hash_table.lookup(self.name)
        user_hash_table.store(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    user_in_group = False

    # Lookup group from group_hash_table
    group_user_hash_table = group_hash_table.lookup(group)

    # If group found, then lookup the user from the retrieved user_hash_table for the group
    if group_user_hash_table:
        user_id = group_user_hash_table.lookup(user)
        if user_id:
            user_in_group = True

    return user_in_group


# Test case 1 - normal case
print("Construct a parent group")
parent = Group("parent")
print("Construct a child group")
child = Group("child")
sub_child = Group("subchild")
print("Add child user to child group")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
print("Add child group to parent group")
child.add_group(sub_child)
parent.add_group(child)

# Should print True
print(is_user_in_group('sub_child_user', 'subchild'))
# Should print False
print(is_user_in_group('sub_child_user', 'parent'))

# Clear hash table
group_hash_table.clear()

# Test case 2 - One group with no user
print("Construct a parent group")
parent = Group("parent")
# Should print False
print(is_user_in_group('sub_child_user', 'parent'))

# Clear hash table
group_hash_table.clear()

# Test case 3 - No group and no user
# Should print False
print(is_user_in_group('sub_child_user', 'parent'))
