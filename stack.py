class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        items = []

        curr = self.top
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        return "->".join(items)

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

        self.size += 1

    def pop(self):
        if self.is_empty(): raise ValueError("Empty Stack!")

        poped_value = self.top.data

        self.top = self.top.next
        self.size -= 1

        return poped_value

    def peek(self):
        if self.is_empty(): raise ValueError("Empty Stack!")
        return self.top.data

    def is_empty(self):
        return self.top is None


if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(11)
    stack.push(12)
    stack.push(13)
    stack.push(14)

    print(stack.peek())
    print()
    print(repr(stack))
    print()
    print(stack.pop())
    print()
    print(stack)
    print()
    print(len(stack))
    print()
    print(stack.is_empty())