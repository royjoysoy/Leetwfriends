class Node:
    def __init__(self.data):
        self.data = data
        self.next = None

    class LinedList:
        def __init__(self):
            init = Node('init')
            self.head = init
            self.tail = init

            self.current = None
            self.length = 0

        def __len__(self):
            return self.length
        
        def append(self. data):
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1