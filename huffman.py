import collections

def huffman_coding(text):
  # Create a frequency table for each character in the text.
  frequency_table = collections.Counter(text)

  # Create a list of tuples, where each tuple contains a character and its frequency.
  characters = frequency_table.items()

  # Sort the list of tuples by frequency, in decreasing order.
  characters.sort(key=lambda x: x[1], reverse=True)

  # Create a list of nodes, where each node represents a character or a combination of characters.
  nodes = []

  # Add each character as a leaf node to the list of nodes.
  for character, frequency in characters:
    nodes.append(Node(character, frequency))

  # While there are more than one node in the list:
  while len(nodes) > 1:
    # Find the two nodes with the lowest frequencies.
    least_frequent_node1 = min(nodes, key=lambda x: x.frequency)
    least_frequent_node2 = min(nodes, key=lambda x: x.frequency)

    # Create a new node that is the parent of the two least frequent nodes.
    new_node = Node(None, least_frequent_node1.frequency + least_frequent_node2.frequency)
    new_node.left = least_frequent_node1
    new_node.right = least_frequent_node2

    # Remove the two least frequent nodes from the list of nodes.
    nodes.remove(least_frequent_node1)
    nodes.remove(least_frequent_node2)

    # Add the new node to the list of nodes.
    nodes.append(new_node)

  # The root node of the Huffman tree is the only node left in the list.
  root_node = nodes[0]

  # Create a dictionary that maps each character to its Huffman code.
  huffman_codes = {}

  # Recursively traverse the Huffman tree to generate the Huffman codes for each character.
  _generate_huffman_codes(root_node, "", huffman_codes)

  # Return the dictionary of Huffman codes.
  return huffman_codes

def _generate_huffman_codes(node, code, huffman_codes):
  # If the node is a leaf node, then add the character to the dictionary of Huffman codes.
  if node.character is not None:
    huffman_codes[node.character] = code

  # Otherwise, recursively traverse the left and right subtrees of the node, adding the appropriate Huffman codes to the dictionary.
  if node.left is not None:
    _generate_huffman_codes(node.left, code + "0", huffman_codes)
  if node.right is not None:
    _generate_huffman_codes(node.right, code + "1", huffman_codes)

class Node:
  def _init_(self, character, frequency):
    self.character = character
    self.frequency = frequency
    self.left = None
    self.right = None