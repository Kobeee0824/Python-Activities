class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed into stack")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        print("Stack:", self.stack)


# Driver Code
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Popped:", s.pop())
print("Top element:", s.peek())
