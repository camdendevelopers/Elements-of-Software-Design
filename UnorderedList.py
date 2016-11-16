class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

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
