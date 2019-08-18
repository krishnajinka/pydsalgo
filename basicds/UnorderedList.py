from Node import Node 

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head 
        count = 0
        while current != None: 
            count += 1
            current = current.getNext()

        return count 

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True 
            else:
                current = current.getNext()
        return found 

    def print(self):
        current = self.head
        mylst = "["
        while current != None:
            mylst = mylst + " " + str(current.getData())
            current = current.getNext()
        mylst = mylst + "]"
        return mylst
    
    def remove(self, item):
        current = self.head 
        previous = None 
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext() 
        if not found:
            return 

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        current = self.head 
        while current.getNext() != None:
            current = current.getNext()

        temp = Node(item)
        current.setNext(temp)

    def insert(self, pos, item):
        current = self.head
        currpos = 0
        previous = None 
        if pos == 0:
            self.add(item)
            return 

        while currpos != pos: 
            previous = current
            current = current.getNext()
            currpos += 1
        
        temp = Node(item)
        temp.setNext(current)
        previous.setNext(temp)
        

        


        
