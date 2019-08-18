from pythonds import Queue
from Printer import Printer
from Task import Task 
import random

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            #print("cursecond is %d"%currentSecond)
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and \
            (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append( \
                nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Avg wait %6.2f secs %3d tasks remaining."%(averageWait, printQueue.size()))

def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True 
    else:
        return False

