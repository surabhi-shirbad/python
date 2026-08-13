import sys

class Queue:

    def __init__(self, queueSize):
        self.queueSize = queueSize
        self.myQueue = []

    def isFull(self):
        return len(self.myQueue) == self.queueSize

    def isEmpty(self):
        return len(self.myQueue) == 0

    def enqueue(self, value):
        if self.isFull():
            print("Queue is full")
        else:
            self.myQueue.append(value)
            print("Element inserted")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Dequeued:", self.myQueue.pop(0))

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("First element:", self.myQueue[0])

    def deleteQueue(self):
        self.myQueue = []
        print("Queue deleted")

    def display(self):
        print("Queue:", self.myQueue)


# Queue 1
size1 = int(input("Enter size of Queue 1: "))
q1 = Queue(size1)

for i in range(size1):
    value = int(input("Enter value for Queue 1: "))
    q1.enqueue(value)


# Queue 2
size2 = int(input("Enter size of Queue 2: "))
q2 = Queue(size2)

for i in range(size2):
    value = int(input("Enter value for Queue 2: "))
    q2.enqueue(value)


# Display queues
print("\nQueue 1:")
q1.display()

print("Queue 2:")
q2.display()


# Combine queues
combinedQueue = q1.myQueue + q2.myQueue

print("Combined Queue:")
print(combinedQueue)