#  File: ERSim.py
#  Description: This program simulates a queue that "performs" treatments on incoming patients
#  Student's Name: Marcos Ortiz
#  Student's UT EID: mjo579
#  Course Name: CS 313E
#  Unique Number: 51320
#
#  Date Created: 10/8/2016
#  Date Last Modified: 10/14/2016

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        s = "[" + ", ".join( [ str(element) for element in self.items]) + "]"
        return s

#Define queues as global variables
fair_queue = Queue()
serious_queue = Queue()
critical_queue = Queue()

#Function that prints queues and their current contents
def queuePrint(queues):
    return "    Queues are:\n    Critical: \t{}\n    Serious: \t{}\n    Fair: \t{}\n".format(queues[0], queues[1], queues[2])

def treatNext(queueList):
    name = ""
    priority = ""

    if not critical_queue.isEmpty():
        name = critical_queue.peek()
        priority = "Critical"
        critical_queue.dequeue()
    elif not serious_queue.isEmpty():
        name = serious_queue.peek()
        priority = "Serious"
        serious_queue.dequeue()
    elif not fair_queue.isEmpty():
        name = fair_queue.peek()
        priority = "Fair"
        fair_queue.dequeue()
    else:
        print("   No patients in queues")
        return

    #print("\n>>> Treat next patient\n")
    print("    Treating {} to {} queue".format(name, priority))
    print(queuePrint(queueList))



#Function to perform activities of each line
def addToQueue(action, instructions):
    queueList = [critical_queue,serious_queue,fair_queue]

    if action == "add":
        name = instructions[0]
        priority = instructions[1]

        if priority == "Fair":
            fair_queue.enqueue(name)
        elif priority == "Serious":
            serious_queue.enqueue(name)
        else:
            critical_queue.enqueue(name)

        print("\n>>> Add patient {} to {} queue".format(name, priority))
        print(queuePrint(queueList))

    elif action == "treat":
        who = instructions[0]

        if who == "next":
            print("\n>>> Treat next patient\n")
            treatNext(queueList)

        elif who == "all":
            print("\n>>> Treat all patients\n")
            for queue in queueList:
                while not queue.isEmpty():
                    treatNext(queueList)

        else: #anything else
            name = ""

            if who == "Fair":
                name = fair_queue.peek()
                fair_queue.enqueue(name)
            elif who == "Serious":
                name = serious_queue.peek()
                serious_queue.enqueue(name)
            elif who == "Critical":
                name = critical_queue.peek()
                critical_queue.enqueue(name)

            print("\n>>> Treat next patient\n")
            print("    Treating {} from {} queue".format(name, who))
            print(queuePrint(queueList))

    else: #Exit
        print("\n>>>Exit")

def main():
    #Get file
    in_file = open("ERSim.txt", "r")

    #Read line by line
    for line in in_file:
        line = line.strip()
        line = line.split()

        #Get what each action is
        action = line[0]
        instructions = line[1:]

        #Perform action based on line
        if action == "add":
            addToQueue(action, instructions)
        elif action == "treat":
            addToQueue(action, instructions)
        else: #Exit
            addToQueue(action, instructions)

main()
