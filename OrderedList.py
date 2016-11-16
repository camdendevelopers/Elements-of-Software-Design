#Ordered List: As you build it, you maintain a specific order to the data items.

class OrderedList():

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        current = self.head
        previous = None
        found False

        while current != None and not found:
            if current.getData() > item:
                found True
            else:
                previous = current
                current = current.getNext(0)

        temp = Node(item)

        if previous == None:
            #Inserting at top of list
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


    def size(self):
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
        #return current

    def remove(self, item):
        current = self.head
        previous = None

        while current.getData != item:
            previous = current
            current = current.getNext()

        if previous == None:
            #We're deleting first item in list
            self.head == current.getNext()
        else:
            previous.setNext(current.getNext())
