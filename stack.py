"""
Structure of comments:
Function description.
Time complexity O()
"""

#Stack Node class - Represents a single node in the Stack data structure.
class Node:
    #Initializes the node with data, and a reference to the next node.
    #Time complexity: O(1)
    def __init__(self, data):
        self.data = data
        self.next = None


#Stack class - Implements a stack data structure using a linked list.
#LIFO (Last In First Out) principle: elements are added and removed from the top.
class Stack:
    #Initializes an empty stack with top pointer set to None and size counter set to 0.
    #Time complexity: O(1)
    def __init__(self):
        self.top = None
        self.size = 0

    #Returns the number of elements currently in the stack.
    #Time complexity: O(1)
    def __len__(self):
        return self.size

    #Returns a string representation of the stack showing all elements from top to bottom.
    #Time complexity: O(n), where n is the number of elements in the stack.
    def __repr__(self):
        if self.is_empty(): return "[]"
        items = []

        curr = self.top
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        items.append("None")
        return "->".join(items)

    #Adds an element to the top of the stack and increases the size counter.
    #Time complexity: O(1)
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

        self.size += 1

    #Removes and returns the element at the top of the stack. Raises ValueError if stack is empty.
    #Time complexity: O(1)
    def pop(self):
        if self.is_empty(): raise ValueError("Empty Stack!")

        popped_value = self.top.data

        self.top = self.top.next
        self.size -= 1

        return popped_value

    #Returns the element at the top of the stack without removing it. Raises ValueError if stack is empty.
    #Time complexity: O(1)
    def peek(self):
        if self.is_empty(): raise ValueError("Empty Stack!")
        return self.top.data

    #Checks if the stack is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self):
        return self.top is None


# if __name__ == "__main__":
#     print("==" * 30, "\nStack data structure:\nBeginning:\n", "__" * 30)
#     stack = Stack()

#     stack.push(10)
#     stack.push(11)
#     stack.push(12)
#     stack.push(13)
#     stack.push(14)

#     print()
#     print(stack.peek())
#     print()
#     print(repr(stack))
#     print()
#     print(stack.pop())
#     print()
#     print(stack)
#     print()
#     print(len(stack))
#     print()
#     print(stack.is_empty())
#     print("==" * 30, "\nStack data structure - End\n")