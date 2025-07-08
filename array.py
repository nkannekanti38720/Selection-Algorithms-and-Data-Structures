# Here I am implementing a basic array with insert, delete, and access methods.
# This allows me to manage a list of elements and perform basic operations.

class Array:
    def __init__(self):
        self.array = []

    # Insert a new element at the end of the array
    def insert(self, value):
        self.array.append(value)

    # Delete an element from the array
    def delete(self, value):
        if value in self.array:
            self.array.remove(value)

    # Access an element at a given index
    def access(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            return None

    # Display the entire array
    def display(self):
        return self.array

# Example usage
arr = Array()
arr.insert(1)
arr.insert(2)
arr.insert(3)
arr.delete(2)
print(arr.display())  # Output: [1, 3]
