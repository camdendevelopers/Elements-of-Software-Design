class Node (object):
   def __init__(self,initdata):
      self.data = initdata
      self.next = None            # always do this – saves a lot
                                  # of headaches later!
   def getData (self):
      return self.data            # returns a POINTER

   def getNext (self):
      return self.next            # returns a POINTER

   def setData (self, newData):
      self.data = newData         # changes a POINTER

   def setNext (self,newNext):
      self.next = newNext         # changes a POINTER

class UnorderedList ():

   def __init__(self):
      self.head = None

   def isEmpty (self):
      return self.head == None

   def add (self,item):
      # add a new Node to the beginning of an existing list
      temp = Node(item)
      temp.setNext(self.head)
      self.head = temp

   def length (self):
      current = self.head
      count = 0

      while current != None:
         count += 1
         current = current.getNext()

      return count

   def search (self,item):
      current = self.head
      found = False

      while current != None and not found:
         if current.getData() == item:
            found = True
         else:
            current = current.getNext()

      return found

   def remove (self,item):
      current = self.head
      previous = None
      found = False

      while not found:
         if current.getData() == item:
            found = True
         else:
            previous = current
            current = current.getNext()

      if previous == None:
         self.head = current.getNext()
      else:
         previous.setNext(current.getNext() )


class OrderedList (object):

   def __init__(self):                # identical to OrderedList
      self.head = None

   def isEmpty (self):                # identical to OrderedList
      return self.head == None

   def length (self):                 # identical to OrderedList
      current = self.head
      count = 0

      while current != None:
         count += 1
         current = current.getNext()

      return count

   def remove (self,item):             # identical to OrderedList
      current = self.head
      previous = None
      found = False

      while not found:
         if current.getData() == item:
            found = True
         else:
            previous = current
            current = current.getNext()

      if previous == None:
         self.head = current.getNext()
      else:
         previous.setNext(current.getNext() )


   def search (self,item):       # improved over UnorderedList.search()

      current = self.head
      found = False
      stop = False
      while current != None and not found and not stop:
         if current.getData() = item:
            found = True
         else:
            if current.getData() > item:
               stop = True
            else:
               current = current.getNext()

      return found

   def add (self,item):       # the only one with a major change from Unordered

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
         temp.setNext(self.head)
         self.head = temp
      else:
         temp.setNext(current)
         previous.setNext(temp)

#
# SENTINEL CODE
#

class UnorderedList (object):

   def __init__(self):
      sentinel = Node(None)
      self.head = sentinel

   def isEmpty (self):
      return self.head.getNext() == None

   def add (self,item):
      # add a new Node to the beginning of an existing list
      temp = Node(item)
      temp.setNext(self.head.getNext())
      self.head.setNext(temp)

   def length (self):
      current = self.head.getNext()
      count = 0

      while current != None:
         count += 1
         current = current.getNext()

      return count

   def search (self,item):
      current = self.head.getNext()
      found = False

      while current != None and not found:
         if current.getData() == item:
            found = True
         else:
            current = current.getNext()

      return found

   def remove (self,item):
      current = self.head.getNext()
      previous = self.head
      found = False

      while not found:
         if current.getData() == item:
            found = True
         else:
            previous = current
            current = current.getNext()

      previous.setNext(current.getNext() )


class OrderedList (object):

   def add (self,item):

      current = self.head.getNext()
      previous = self.head
      stop = False

      while current != None and not stop:
         if current.getData() > item:
            stop = True
         else:
            previous = current
            current = current.getNext()

      temp = Node(item)
      temp.setNext(current)
      previous.setNext(temp)
