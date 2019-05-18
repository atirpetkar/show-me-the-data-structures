# Problem 2 - Union and Intersection - Explanation

To improve efficiency, a hash table eas used to perform lookup of a value.

For union, we traverse both list, lookup the hash table and build the result list.

The run time complexity analysis is as follows:
1. Calculate hash value (O(n))
1. Lookup value from hash table (O(1))
1. Store value to hash table (O(1))

So the overall run time complexity of union operation is O(n)

For intersection, we traverse first list, build the hash table.
Then we traverse second list, check hash table. If found, then it's added into the intersection list.

The run time complexity analysis is as follows:
1. Calculate hash value (O(n))
1. Lookup value from hash table (O(1))
1. Store value to hash table (O(1))
1. Check whether the value is in a Python list to eliminate duplicate values (O(n))

So the overall run time complexity of intrsection operation is O(n)
