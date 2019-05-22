from collections import Counter


class HuffmanNode(object):
    """
    A class represent a node in Huffman tree
    """
    def __init__(self, data=None, node_type=None, frequency=None):
        # A node can be a frequency node or char node (i.e. the character)
        self.node_type = node_type
        self.data = data
        self.frequency = frequency
        self.left = None
        self.right = None

    def __str__(self):
        output_str = f"------Node type: {self.node_type}, data: {self.data}, frequency: {self.frequency}------\n"

        # if self.left:
        #     output_str += f">>>>>>Left node: {self.left.data}<<<<<<<<<<<\n"
        # if self.right:
        #     output_str += f">>>>>>Right node: {self.right.data}<<<<<<<<<<<\n"

        return output_str


class HuffmanTree(object):
    """
    A class representing a Huffman tree
    """
    def __init__(self):
        self.root = None

    def __repr__(self):
        node_str_list = list()

        def traverse(node):
            if node is None:
                return

            node_str_list.append(str(node))

            if node.left:
                print(f">>>>>>>>>>>>>>>>left: {node.left.data}")
            traverse(node.left)
            if node.right:
                print(f">>>>>>>>>>>>>>>>right: {node.right.left}")
            traverse(node.right)

        traverse(self.root)

        output_str = '\n'.join(node_str_list)

        return output_str


def build_sub_tree_from_tuples(tuple_left, tuple_right):
    """
    Build a Huffman tree from 2 tuples
    :param tuple_left:
    :param tuple_right:
    :return:
    """

    sub_tree = HuffmanTree()

    # Check whether the tuple is a char or already merged tree
    tuple_left_data = tuple_left[0]
    tuple_left_freq = tuple_left[1]

    if isinstance(tuple_left_data, str):
        huff_node_left = HuffmanNode(data=tuple_left_data, node_type='character', frequency=tuple_left_freq)
    else:
        huff_node_left = HuffmanNode(data=tuple_left_data.root, node_type='frequency', frequency=tuple_left_freq)

    # Check whether the tuple is a char or already merged tree
    tuple_right_data = tuple_right[0]
    tuple_right_freq = tuple_right[1]

    if isinstance(tuple_right_data, str):
        huff_node_right = HuffmanNode(data=tuple_right_data, node_type='character', frequency=tuple_right_freq)
    else:
        huff_node_right = HuffmanNode(data=tuple_right_data.root, node_type='frequency', frequency=tuple_right_freq)

    # Construct a summary frequency node
    freq_sum = tuple_left_freq + tuple_right_freq

    summary_freq_node = HuffmanNode(node_type='frequency', frequency=freq_sum)
    summary_freq_node.left = huff_node_left
    summary_freq_node.right = huff_node_right
    sub_tree.root = summary_freq_node

    # print(f"sub-tree: {sub_tree}")

    return sub_tree, freq_sum


def build_huffman_tree(data):
    """
    Build a Huffman tree base on the data argument
    :param data: data to build tree
    :return: the Huffman tree
    """
    huffman_tree = HuffmanTree()

    # Convert the input data into a list of tuples, sorted by frequency
    print(f"Input data: {data}")

    input_str_char_counter = Counter(input_str)

    input_str_char_freq_tuple_list = list()

    for key, value in input_str_char_counter.items():
        input_str_char_freq_tuple_list.append((key, value))

    # Sort tuple by char frequency
    input_str_char_freq_tuple_list.sort(key=lambda r: r[1])

    print(input_str_char_freq_tuple_list)

    while len(input_str_char_freq_tuple_list) > 1:
        # Retrieve the first 2 tuples with lowest frequencies
        char_freq_tuple_left = input_str_char_freq_tuple_list.pop(0)
        # print(f"char_freq_tuple_left: {char_freq_tuple_left}")

        char_freq_tuple_right = input_str_char_freq_tuple_list.pop(0)
        # print(f"char_freq_tuple_right: {char_freq_tuple_right}")

        # Build a subtree from the list
        sub_tree, freq_sum = build_sub_tree_from_tuples(char_freq_tuple_left, char_freq_tuple_right)

        # Add merged tree into tuple list
        input_str_char_freq_tuple_list.append((sub_tree, freq_sum))

        # Sort the list again
        input_str_char_freq_tuple_list.sort(key=lambda r: r[1])
        # print(input_str_char_freq_tuple_list)

    huffman_tree = input_str_char_freq_tuple_list[0]

    return huffman_tree


# input_str = "The bird is the word"
input_str = "abc"

huffman_tree = build_huffman_tree(input_str)
print(huffman_tree)
