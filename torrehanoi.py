class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def apilar(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def desapilar(self):
        if not self.top:
            return None
        node = self.top
        self.top = node.next
        return node.value

    def cima(self):
        return self.top.value if self.top else None

def move_aguja(height, from_stack, to_stack, with_stack):
    """
    >>> move_tower(3, Stack(), Stack(), Stack())
    moving disk from A to B
    moving disk from A to C
    moving disk from B to C
    moving disk from A to B
    moving disk from C to A
    moving disk from C to B
    moving disk from A to B
    """
    if height >= 1:
        move_aguja(height - 1, from_stack, with_stack, to_stack)
        move_disk(from_stack, to_stack)
        move_aguja(height - 1, with_stack, to_stack, from_stack)

def move_disk(from_stack, to_stack):
    disk = from_stack.desapilar()
    to_stack.apilar(disk)
    print("moving disk from", from_stack.name, "to", to_stack.name)

def main():
    height = int(input("Height of hanoi: ").strip())

    # Create stacks
    stack_a = Stack()
    stack_a.name = 'A'
    stack_b = Stack()
    stack_b.name = 'B'
    stack_c = Stack()
    stack_c.name = 'C'
    for i in range(height, 0, -1):
        stack_a.apilar(i)

    move_aguja(height, stack_a, stack_b, stack_c)

if __name__ == "__main__":
    main()

     