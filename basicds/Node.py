class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, item):
        self.data = item

    def setNext(self, newNode):
        self.next = newNode
