# Problem 4 - Active Directory - Explanation

## Implementation
To implement an efficient lookup mechanism for whether a user is in a group, hash table was used:
1. All the groups will be stored into a hash table for quick lookup.
1. For each group, a child hash table was used to store the users in that group, by using their user id's hash values as index.
1. For each lookup, the group will be retrieved from the group hash table, and then user from the group's user hash table.

## Run time complexity
Both the group and user were being looked up from hash table, which requires constant time.

As a result, the run time complexity for checking whether a user is in a group is of O(1).
