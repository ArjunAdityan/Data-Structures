class Node:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorderTraversal(root):
    if root is None:
        return []

    stack1 = []
    stack2 = []
    stack1.append(root)

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    result = []
    while stack2:
        node = stack2.pop()
        result.append(node.value)

    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

result = postorderTraversal(root)
print(result)  # Output: [4, 5, 2, 3, 1]
class Node:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorderTraversal(root):
    result = []
    if root:
        result = inorderTraversal(root.left)
        result.append(root.value)
        result += inorderTraversal(root.right)
    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

result = inorderTraversal(root)
print(result)
class Node:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorderTraversal(root):
    result = []
    if root:
        result.append(root.value)
        result += preorderTraversal(root.left)
        result += preorderTraversal(root.right)
    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

result = preorderTraversal(root)
print(result)