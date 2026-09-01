# Stack Data Structure

A simple Python implementation of a stack using a linked list.

## Overview

This project implements a Stack data structure following the LIFO (Last In, First Out) principle:

- `push(data)` adds an element to the top
- `pop()` removes and returns the top element
- `peek()` returns the top element without removing it
- `is_empty()` checks whether the stack is empty
- `__len__()` returns the current size of the stack

The implementation is built with a `Node` class and a `Stack` class in [stack.py](stack.py).

## Features

- Efficient stack operations
- Constant-time push, pop, and peek
- Simple linked-list-based design
- Clear example usage inside the file

## Time Complexity

- `push`: O(1)
- `pop`: O(1)
- `peek`: O(1)
- `is_empty`: O(1)
- `__repr__`: O(n)

## Usage

```python
from stack import Stack

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())  # 30
print(len(stack))    # 3
print(stack.pop())   # 30
print(repr(stack))   # 20->10
```

## Running the Example

From the project folder, run:

```bash
python stack.py
```

This will demonstrate a basic stack example in the terminal.

## Project Structure

```text
Stack/
├── stack.py
├── README.md
```

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## Author

Ismail - [@Imismail18](https://github.com/Imismail18)

## License

MIT License

Copyright (c) 2026 Ismail

This project is provided for learning and educational purposes.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.





