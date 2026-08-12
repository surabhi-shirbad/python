# pop= it remove element permently
#  peek = it return top of the element
#  isEmpty= it delet the element from the stack
# isFull=
# array , List= is to implment ,speed problem  when it grows
#   List,linkedList = fast peformance ,  hard implementation
# Using list or array
import sys

class Stack:
    # Constructor - it creates and initializes the stack
    def __init__(self, stackSize):
        self.stackSize = stackSize
        self.myStack = []   # list represents the stack in Python

    def isFull(self):
        if len(self.myStack) == self.stackSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.myStack == []:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            print("Stack is full")
        else:
            self.myStack.append(value)
            print("Element pushed")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Element popped:", self.myStack.pop())

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Top element:", self.myStack[-1])

    def deleteStack(self):
        self.myStack = []
        print("Stack has been deleted")

    def display(self):
        print("Stack:", self.myStack)


size = int(input("Enter the size of the stack: "))
obj = Stack(size)   # Object created for Stack class

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. IsFull")
    print("5. IsEmpty")
    print("6. Delete Stack")
    print("7. Display Stack")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to push into the stack: "))
        obj.push(value)

    elif choice == 2:
        obj.pop()

    elif choice == 3:
        obj.peek()

    elif choice == 4:
        print(obj.isFull())

    elif choice == 5:
        print(obj.isEmpty())

    elif choice == 6:
        obj.deleteStack()

    elif choice == 7:
        obj.display()

    else:
        sys.exit()

    