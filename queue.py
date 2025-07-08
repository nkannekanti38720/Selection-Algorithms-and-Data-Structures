# I am implementing a queue using a Python list.
# A queue works on a First-In-First-Out (FIFO) principle.

class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue an element into the queue
    def enqueue(self, value):
        self.queue.append(value)

    # Dequeue an element from the queue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    # Peek at the front element of the queue
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
