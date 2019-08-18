class Stack:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

    def size(self):
        if self.items:
            return len(self.items)

    def peek(self):
        if self.items:
            return self.items[len(self.items)-1]


