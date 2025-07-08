# Here, I am implementing a singly linked list with insert, delete, and display methods.
# This structure allows dynamic memory allocation and easy insertion/deletion.

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the beginning of the linked list
    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Delete a node with a given value
    def delete(self, value):
        temp = self.head
        if temp and temp.value == value:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.value != value:
            prev = temp
            temp = temp.next

        if not temp:
            return

        prev.next = temp.next
        temp = None

    # Display all nodes in the linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.delete(2)
linked_list.display()  # Output: 3 -> 1 -> None
