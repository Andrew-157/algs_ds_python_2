
def create_stack():
    stack = []
    return stack


def check_empty(stack):
    return len(stack) == 0


def push(stack: list, item):
    stack.append(item)
    print(f'Pushed item: {item}')


def pop(stack: list):
    if check_empty(stack):
        return "Stack is empty"
    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))


"""
Stack Time Complexity
For the array-based implementation of a stack, the push and pop operations take constant time, i.e. O(1).


"""
