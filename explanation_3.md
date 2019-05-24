# Problem 3 - Huffman Coding - Explanation

## Implementation
1. Python's Counter class from collections module was used to count the frequency of each characters
1. Python's dict and tuples were used to store the data for building the Huffman tree
1. In building the Huffman tree, the 2 elements with the lowest frequencies were removed from the tuple list, build a Huffman sub-tree, and insert back into the tuple list
1. The above process was repeated until all the elements were merged
1. The resulting Huffman tree is like a binary tree

## Run time complexity

### Encoding
For encoding, the most time consuming process is to construct the Huffman tree from the tuple of character/Huffman sub-tree and their frequencies.
The complexity is of O(n^2)

### Decoding
For decoding, the most time consuming processing is to processing each bit in the encoded data, traverse the Huffman tree and locate the corresponding character
The complexity is of O(n), where n is the size of the encoded data
