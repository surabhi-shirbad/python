# In left side: values less than or equal to root
# In right side: values greater than root

class BST:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


# Insert node into BST
def insertNode(rootNode, nodeValue):

    # If tree is empty
    if rootNode.data is None:
        rootNode.data = nodeValue

    # Insert in left subtree
    elif nodeValue <= rootNode.data:

        if rootNode.leftchild is None:
            rootNode.leftchild = BST(nodeValue)
        else:
            insertNode(rootNode.leftchild, nodeValue)

    # Insert in right subtree
    else:

        if rootNode.rightchild is None:
            rootNode.rightchild = BST(nodeValue)
        else:
            insertNode(rootNode.rightchild, nodeValue)


# Preorder Traversal
# Root -> Left -> Right
def preOrderTraversal(rootNode):
    if rootNode is None:
        return

    print(rootNode.data, end=" ")
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)


# Inorder Traversal
# Left -> Root -> Right
def inOrderTraversal(rootNode):
    if rootNode is None:
        return

    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data, end=" ")
    inOrderTraversal(rootNode.rightchild)


# Postorder Traversal
# Left -> Right -> Root
def postOrderTraversal(rootNode):
    if rootNode is None:
        return

    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data, end=" ")


# Create empty BST
bstobj = BST(None)

# Insert nodes
insertNode(bstobj, 70)
insertNode(bstobj, 50)
insertNode(bstobj, 90)
insertNode(bstobj, 30)
insertNode(bstobj, 60)
insertNode(bstobj, 80)
insertNode(bstobj, 100)
insertNode(bstobj, 20)
insertNode(bstobj, 40)
insertNode(bstobj, 10)


# Display traversals
print("Preorder:")
preOrderTraversal(bstobj)

print("\nInorder:")
inOrderTraversal(bstobj)

print("\nPostorder:")
postOrderTraversal(bstobj)