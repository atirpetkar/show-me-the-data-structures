class HuffmanTree(object):
    """
    A class representing a Huffman tree
    """
    def __init__(self):
        self.root = None


input_tree = HuffmanTree()

input_tuple_list = [('T', 1), ('a', 2)]

tuple_element = input_tuple_list.pop(0)

print(tuple_element)
print(input_tuple_list)

print(isinstance('T', str))
print(isinstance(input_tree, HuffmanTree))

