import queue

MAX_SIZE = 100


class HuffmanTreeNode:
    def _init_(self, character, frequency):
        # Stores character
        self.data = character

        # Stores frequency of the character
        self.freq = frequency

        # Left child of the current node
        self.left = None

        # Right child of the current node
        self.right = None

    def _lt_(self, other):
        return self.freq < other.freq


# Function to generate Huffman Encoding Tree
def generateTree(pq):
    # We keep on looping till only one node remains in the Priority Queue
    while pq.qsize() != 1:
        # Node which has least frequency
        left = pq.get()

        # Node which has least frequency
        right = pq.get()

        # A new node is formed with frequency left.freq + right.freq
        # We take data as '$' because we are only concerned with the frequency
        node = HuffmanTreeNode('$', left.freq + right.freq)
        node.left = left
        node.right = right

        # Push back node created to the Priority Queue
        pq.put(node)

    return pq.get()


# Function to print the huffman code for each character.
# It uses arr to store the codes
def printCodes(root, arr, top):
    # Assign 0 to the left node and recur
    if root.left:
        arr[top] = 0
        printCodes(root.left, arr, top + 1)

    # Assign 1 to the right node and recur
    if root.right:
        arr[top] = 1
        printCodes(root.right, arr, top + 1)

    # If this is a leaf node, then we print root.data
    # We also print the code for this character from arr
    if not root.left and not root.right:
        print(root.data, end=' ')
        for i in range(top):
            print(arr[i], end='')
        print()


def HuffmanCodes(data, freq, size):
    pq = queue.PriorityQueue()

    for i in range(size):
        newNode = HuffmanTreeNode(data[i], freq[i])
        pq.put(newNode)

    root = generateTree(pq)

    # Print Huffman Codes
    arr = [0] * MAX_SIZE
    top = 0
    printCodes(root, arr, top)


str_enc = input('Enter the string to encode: ')
data = []
for i in str_enc:
    if i not in data:
        data.append(i)
print(data)
freq = []
count = 1
s = {}
for i in str_enc:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1
for i in s:
    freq.append(s.get(i))
print(freq)

size = len(data)
HuffmanCodes(data, freq, size)