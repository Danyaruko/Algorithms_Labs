class Node():
    def __init__(self, value):
        self.next_node = None
        self.previous_node = None
        self.value = value
    
    def __str__(self):
        f"Nodes value: {self.value}"\
        f"Next node: {self.next_node}"\
        f"Previous node: {self.previous_node}"

class Stack():
    def __init__(self):
        self.top = None
        self.head = None
        self.length = 0

    def __str__(self):
        current_node = self.head
        counter = 0
        if self.length == 0:
            return print("The stack is empty; Nothing to print!")
        while current_node != None:
            print("Node value in position", counter,
            "is:", current_node.value, sep=' ')
            current_node = current_node.next_node
            counter += 1
        return 'End of the stack'

    def push(self, value):
        node_to_push = Node(value)
        if self.top == None:
            self.top = node_to_push
            self.head = node_to_push
        else:
            self.top.next_node = node_to_push
            node_to_push.previous_node = self.top
            self.top = node_to_push
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            print("The stack is empty; Nothing to pop!")
        else:
            node_to_pop = self.top
            self.top = self.top.previous_node
            self.top.next_node = None
        self.length -= 1
        return node_to_pop

    def peek(self):
        print("The top element of the stack is:", self.top.value)
        return self.top.value

    def search(self, value):
        if self.length == 0:
            print("The stack is empty; Nothing to search!")
        else: 
            current_node = self.head
            counter = 0
            while current_node != None:
                if current_node.value == value: 
                    print("Found value:", 
                    value, "in position: ", counter, sep=' ')
                    return (value, counter)
                elif current_node.next_node != None:
                    current_node = current_node.next_node
                    counter += 1
                else:
                    return print("Value not found")



