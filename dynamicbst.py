# In left side: values less than or equal to root
# In right side: values greater than root

class BST:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


def insertNode(rootNode, nodeValue):#o(logN)

    if rootNode.data is None:
        rootNode.data = nodeValue

    elif nodeValue <= rootNode.data:

        if rootNode.leftchild is None:
            rootNode.leftchild = BST(nodeValue)
        else:
            insertNode(rootNode.leftchild, nodeValue)

    else:

        if rootNode.rightchild is None:
            rootNode.rightchild = BST(nodeValue)
        else:
            insertNode(rootNode.rightchild, nodeValue)


def preOrderTraversal(rootNode):
    if rootNode is None:
        return

    print(rootNode.data, end=" ")
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)

def inOrderTraversal(rootNode):
    if rootNode is None:
        return

    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data, end=" ")
    inOrderTraversal(rootNode.rightchild)


def postOrderTraversal(rootNode):
    if rootNode is None:
        return

    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data, end=" ")


bstobj = BST(None)

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


print("Preorder:")
preOrderTraversal(bstobj)

print("\nInorder:")
inOrderTraversal(bstobj)

print("\nPostorder:")
postOrderTraversal(bstobj)