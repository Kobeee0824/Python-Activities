class Queue:
    def __init__(self):
        self.items = []  # List to store queue elements

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)  # Add item to the end of the queue
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue.")
            return None
        item = self.items.pop(0)  # Remove item from the front
        print(f"Dequeued: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.items[0]  # Front element

    def size(self):
        return len(self.items)

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(f"Front item: {q.peek()}")  # Should print 10

q.dequeue()  # Removes 10
q.dequeue()  # Removes 20

print(f"Queue size: {q.size()}")
q.dequeue()  # Removes 30
q.dequeue()  # Queue is empty
