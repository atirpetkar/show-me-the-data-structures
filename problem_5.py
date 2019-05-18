import hashlib
import time


class Block(object):
    """
    Block class
    - every block will maintain a reference to the previous block within a chain
    """

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev = None

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        block_str = f"Timestamp: {self.timestamp}, Data: {self.data}, Hash: {self.hash}, Previous hash: {self.previous_hash}"
        return block_str


class Blockchain(object):
    """
    Blockchain class with the following attributes:
    - head: pointing to the head of the chain
    - tail: pointing to the last Block
    """

    def __init__(self, genesis=None):
        # Normally a Blockchain will be initialize with the first (genesis) block
        if genesis is None:
            self.head = None
            self.tail = None
        else:
            self.head = genesis
            self.tail = genesis

    def append(self, data):
        """
        Append a new block into the chain with the provided data
        :param data:
        :return:
        """

        # Retrieve the hash from the tail block
        if self.tail:
            previous_hash = self.tail.hash
        else:
            previous_hash = None

        # Compute the current GMT time
        current_time_gmt = time.gmtime()

        # Construct a new Block
        new_block = Block(current_time_gmt, data, previous_hash)

        if self.tail is None:
            self.head = new_block
            self.tail = new_block
        else:
            new_block.prev = self.tail
            self.tail = new_block

    def __repr__(self):
        cur_block = self.tail

        blockchain_str = "Blockchain content:\n"

        while cur_block:
            blockchain_str += "Block:\n"
            blockchain_str += str(cur_block) + "\n"
            cur_block = cur_block.prev

        return blockchain_str


# Test case 1
print(f"Test case 1 - initialize an empty block chain")
block_chain = Blockchain()
# Should print Blockchain content:, and then an empty line
print(block_chain)

# Test case 2
print(f"Test case 2 - Add the first block with data: 'I am the first block'")
block_chain.append("I am the first block")
# Should print Blockchain content:, and then the block with data "I am the first block"
print(block_chain)

# Test case 3
print(f"Test case 3 - Add one more block to chain with data 'I am the last block'")
block_chain.append("I am the last block")
# Should print Blockchain content:, and then the block with data "I am the last block", then the block with data "I am the first block"
print(block_chain)
