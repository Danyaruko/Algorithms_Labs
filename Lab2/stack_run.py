from stack import Stack
from stack import Node

stack_example = Stack()

stack_example.push(4)
stack_example.push(7)
stack_example.push(8)
stack_example.push(3)
stack_example.push(6)
stack_example.push(40)

print(stack_example)

stack_example.search(6)
stack_example.peek()

stack_example.pop()
stack_example.pop()

stack_example.peek()

stack_example.search(6)