# Problem 5 - Blockchain - Explanation

The Blockchain class was implemented as a linked list. Each Blockchain have a pointer to both the head and tail block of the chain. And each block will have a reference to the previous block and it's hash value.

## Run time complexity
The main operation is the calculation of the hash value, which is of constant time.

As a result, the complexity for adding a block to the chain is O(1)
