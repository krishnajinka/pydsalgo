from Node import Node 
class OrderedList:
    def __init__(self):
        self.head = None 
    
    def isEmpty(self):
        return self.head == None
    
    def length(self):
        current = self.head
        count = 0
        while current != None:
            current = current.getNext()
            count += 1
        return count 

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop: 
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext() 

        temp = Node(item)
        if previous == None:
            temp.setNext(current)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def print(self):
        current = self.head
        mylst = "["
        while current != None:
            mylst = mylst + " " + str(current.getData())
            current = current.getNext()
        mylst = mylst + "]"
        return mylst
