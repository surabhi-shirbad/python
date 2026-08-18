class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None       # Starting node
        self.tail = None       # Last node

    # Add node at the end
    def addNodeEnd(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Display linked list
    def display(self):
        current = self.head

        while current is not None:
            print("|", current.data, "| -> ", end="")
            current = current.next

        print("")

    # Add node at the beginning
    def addNodeBegin(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Search node
    def searchNode(self, target):
        current = self.head

        while current is not None:
            if current.data == target:
                return True

            current = current.next
        return False

    def addNodeinbetween(self, index, Value):

        new_node = Node(Value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        elif index == 0:
            new_node.next = self.head
            self.head = new_node

        else:
            temp = self.head

        for i in range(index - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        if new_node.next is None:
            self.tail = new_node
            
    def deletefirst(self):
        if self.head is None:
            print("list is empty")
            return
        self.head=self.head.next  

        if self.head is None:
            self.tail=None  

    def deletelast(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head== self.tail:
            self.head= None
            self.tail=None
        current =self.head   
        while current.next != self.tail:
            current=current.next
        current.next=None
        self.tail=current


linkedlistobj = LinkedList()

linkedlistobj.addNodeEnd(10)
linkedlistobj.addNodeEnd(20)
linkedlistobj.addNodeEnd(30)
linkedlistobj.addNodeEnd(40)

linkedlistobj.display()


linkedlistobj.addNodeBegin(5)

print("After adding 5 at beginning:")
linkedlistobj.display()


if linkedlistobj.searchNode(20):
    print("20 is found")
else:
    print("20 is not found")

linkedlistobj.deletefirst()
linkedlistobj.display()
linkedlistobj.deletelast()
linkedlistobj.display()
linkedlistobj.addNodeinbetween(2,90)
linkedlistobj.display()

