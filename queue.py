import sys

class Queue:

    # Constructor
    def __init__(self, queueSize):
        self.queueSize = queueSize
        self.myQueue = []

    # Check if queue is full
    def isFull(self):
        if len(self.myQueue) == self.queueSize:
            return True
        else:
            return False

    # Check if queue is empty
    def isEmpty(self):
        if self.myQueue == []:
            return True
        else:
            return False

    # Add element to queue
    def enqueue(self, value):
        if self.isFull():
            print("Queue is full")
        else:
            self.myQueue.append(value)
            print("Element inserted")

    # Remove first element
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Dequeued element:", self.myQueue.pop(0))

    # Return first element
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("First element:", self.myQueue[0])

    # Delete entire queue
    def deleteQueue(self):
        self.myQueue = []
        print("Queue has been deleted")

    # Display queue
    def display(self):
        print("Queue:", self.myQueue)


# Main program
size = int(input("Enter the size of queue: "))

obj = Queue(size)

while True:

    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. IsEmpty")
    print("5. IsFull")
    print("6. Delete entire queue")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to insert into queue: "))
        obj.enqueue(value)

    elif choice == 2:
        obj.dequeue()

    elif choice == 3:
        obj.peek()

    elif choice == 4:
        print(obj.isEmpty())

    elif choice == 5:
        print(obj.isFull())

    elif choice == 6:
        obj.deleteQueue()

    elif choice == 7:
        obj.display()

    elif choice == 8:
        print("Program exited")
        sys.exit()

    else:
        print("Invalid choice")