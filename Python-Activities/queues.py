class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} enqueued")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
        else:
            return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.queue[0]

    def size(self):
        return len(self.queue)

    def display(self):
        print("Queue:", self.queue)


# Driver Code
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("Dequeued:", q.dequeue())
print("Front element:", q.front())
