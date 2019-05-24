import sys
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

            traverse(node.left)
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
        huff_node_left = tuple_left_data.root

    # Check whether the tuple is a char or already merged tree
    tuple_right_data = tuple_right[0]
    tuple_right_freq = tuple_right[1]

    if isinstance(tuple_right_data, str):
        huff_node_right = HuffmanNode(data=tuple_right_data, node_type='character', frequency=tuple_right_freq)
    else:
        huff_node_right = tuple_right_data.root

    # Construct a summary frequency node
    freq_sum = tuple_left_freq + tuple_right_freq

    summary_freq_node = HuffmanNode(node_type='frequency', frequency=freq_sum)
    summary_freq_node.left = huff_node_left
    summary_freq_node.right = huff_node_right
    sub_tree.root = summary_freq_node

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

    input_str_char_counter = Counter(data)

    input_str_char_freq_tuple_list = list()

    for key, value in input_str_char_counter.items():
        input_str_char_freq_tuple_list.append((key, value))

    # Sort tuple by char frequency
    input_str_char_freq_tuple_list.sort(key=lambda r: r[1])

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

    if len(input_str_char_freq_tuple_list) > 0:
        huffman_tree = input_str_char_freq_tuple_list[0][0]

    return huffman_tree


def trim_huffman_tree(huffman_tree):
    """
    Trim a Huffman tree by setting all node's frequency to zero
    :param huffman_tree:
    :return: trimmed Huffman tree
    """

    def trim_node_frequency(node):

        if node is None:
            return

        # Reset frequency to zero
        node.frequency = 0

        trim_node_frequency(node.left)
        trim_node_frequency(node.right)

    trim_node_frequency(huffman_tree.root)

    return huffman_tree


def encode_data_with_huffman_tree(huffman_tree, data):
    """
    Encode data with the provided Huffman Tree
    :param huffman_tree: trimmed Huffman Tree
    :param data: the data to encode
    :return: Huffman tree, encoded data
    """
    encoded_data = ""

    if huffman_tree.root is None:
        return huffman_tree, encoded_data

    # A dict to store the mapping of each character to Huffman code
    char_code_dict = dict()

    def build_char_code_dict(node, char_code):
        if node.node_type == 'character':
            char_code_dict[node.data] = char_code
            return

        if node.left:
            char_code += '0'
            build_char_code_dict(node.left, char_code)

        if node.right:
            char_code = char_code[:-1]
            char_code += '1'
            build_char_code_dict(node.right, char_code)

    build_char_code_dict(huffman_tree.root, "")

    # Encode data
    for char in data:
        encoded_data += char_code_dict[char]

    return huffman_tree, encoded_data


def huffman_encoding(data):

    # Build Huffman tree using the data
    huffman_tree = build_huffman_tree(data)

    # Trim Huffman tree
    trimmed_huffman_tree = trim_huffman_tree(huffman_tree)

    # Encoding data using Huffman tree
    huffman_tree, encoded_data = encode_data_with_huffman_tree(trimmed_huffman_tree, data)

    return encoded_data, huffman_tree


def huffman_decoding(data, tree):
    """
    Perform decoding base on encoded data and a Huffman Tree
    :param data: encoded data
    :param tree: Huffman tree for the encoded data
    :return: decoded data
    """

    decoded_data = ""

    encoded_data = data

    current_node = tree.root

    encoded_bit_stream = ""
    while True:
        if len(encoded_data) == 0:
            break

        encoded_bit = encoded_data[0]
        encoded_data = encoded_data[1:]

        if encoded_bit == '0':
            nav_direction = 'left'
        else:
            nav_direction = 'right'

        encoded_bit_stream += encoded_bit

        if nav_direction == 'left':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.node_type == 'character':
            decoded_data += current_node.data

            current_node = tree.root
            encoded_bit_stream = ""

    return decoded_data


if __name__ == "__main__":
    codes = {}

    print("Test case 1 - normal sentence")
    print("Input: The bird is the word")
    a_great_sentence = "The bird is the word"

    # Should print 69
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Should print "The bird is the word"
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # Should print 36
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Should print 0110111011111100111000001010110000100011010011110111111010101011001010
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    # Should print 69
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Should print "The bird is the word"
    print("The content of the decoded data is: {}\n".format(decoded_data))

    print("Test case 2 - empty sentence")
    a_great_sentence = ""

    # Should print 49
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Should print empty line
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # Should print empty string
    print("The content of the encoded data is: {}\n".format(encoded_data))
