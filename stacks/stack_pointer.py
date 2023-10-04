# Stack implementation with TOP pointer

class StackIsFullException(Exception):
    pass


class StackIsEmptyException(Exception):
    pass


class Stack:
    def __init__(self):
        self.stack: dict = {}
        self.top: int = -1
        self.stack_size: int = 5

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.stack_size - 1

    def push(self, element):
        if self.is_full():
            raise StackIsFullException
        self.top += 1
        self.stack[self.top] = element

    def pop(self):
        if self.is_empty():
            raise StackIsEmptyException
        to_return = self.stack.pop(self.top)
        self.top -= 1
        return to_return

    def peek(self):
        if self.is_empty():
            raise StackIsEmptyException
        return self.stack[self.top]

    def show(self):
        return list(self.stack.values())


stack = Stack()

stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.show())
print(stack.pop())
print(stack.show())
print(stack.peek())
