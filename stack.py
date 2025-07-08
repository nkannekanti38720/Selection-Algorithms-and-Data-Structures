# In this implementation, I am creating a stack using a Python list.
# A stack works on a Last-In-First-Out (LIFO) principle.

class Stack:
    def __init__(self):
        self.stack = []

    # Push an element onto the stack
    def push(self, value):
        self.stack.append(value)

    # Pop an element from the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    # Peek at the top element of the stack
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
