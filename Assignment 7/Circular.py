#  File: Circular.py
#  Description: This program simulates the hot potato game using circular linked lists
#  Student's Name: Marcos Ortiz
#  Student's UT EID: mjo579
#  Course Name: CS 313E
#  Unique Number: 51320
#
#  Date Created: 10/25/2016
#  Date Last Modified: 10/28/2016

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

class CircularList(object):

   def __init__ (self):
      # the circular list constructor method.
      sentinel = Node(None)
      self.head = sentinel
      self.head.setNext(self.head)
      self.count = 0
      self.nextDeleted = None

   def add (self,item):
      # Insert an element in the list.  You will need this to build your
      # circular list from the data strings in the input file.  Hint:  figure
      # out which of the "add" methods we've discussed in class to use is
      # useful here and use it as a template for this method.
      current = self.head.getNext()
      previous = self.head
      stop = False

      while current != self.head:
          previous = current
          current = current.getNext()

      temp = Node(item)
      temp.setNext(self.head)
      previous.setNext(temp)
      self.count += 1


   def isEmpty (self):
      # Return True if the cicrcular list is empty.
      return self.head.getNext() == self.head

   def onlyOneNode (self):
      # Return True if there is only one node left in the circular list.
      # This would be the "survivor".
      return self.count == 1

   def length (self):
       # Return True if there is only one node left in the circular list.
       # This would be the "survivor".
       return self.count

   def remove (self, n):
      # ATTENTION: This method is different because it takes in the
      # hit number as a parameter so that in the main function the loop
      # continues to remove people using the hit number until there is
      # only one person standing.
      previous = None
      if self.nextDeleted == None or self.nextDeleted == self.head:
          current = self.head
          count = 0
      else:
          current = self.nextDeleted
          count = 1

      while count < n:
          previous = current
          current = current.getNext()
          if current == self.head:
              previous = current
              current = current.getNext()
          count += 1

      previous.setNext(current.getNext())
      self.nextDeleted = previous.getNext()

      self.count -= 1

      return current.getData()

   def __str__ (self):
      # Return a string representation of the circular list.  It should
      # include line breaks after every ten elements in the list.
      current = self.head.getNext()
      elementCount = 0
      string = ""

      while current != self.head:
          if elementCount % 10 == 0:
              string += "\n" + str(current.getData()) + "   "
          else:
              string += str(current.getData()) + "  "

          current = current.getNext()
          elementCount += 1

      return string

def main():
    # 1. Open file
    in_file = open("HotPotatoData.txt", "r")

    # 2. Read first line
    line = in_file.readline()
    on_line = 1

    # 3. Interate through the file, reading line by line
    while line != "":

        # 4. Strip the line of any new line characters
        line = line.strip()

        # 5. If line contains number (instructions)
        if line[0].isnumeric():
            people = CircularList()
            line = line.split()
            numPeople = int(line[0])
            hitNumber = int(line[1])

            print("\nLet the games begin:")
            print("--------------------\n")
            print("Number of players: ", numPeople)
            print("Hit number: ", hitNumber)

            # 6. Begin a game
            for i in range(numPeople):
                person = in_file.readline()
                person = person.strip()
                people.add(person) # Add people to the list

            round_num = 1
            print("Initial players\n", people)
            while people.length() >= 2:
                victim = people.remove(hitNumber)
                print("\nRound number: ", round_num)
                print("Person lost: ", victim)
                print("People left:", people)
                round_num += 1

            if people.onlyOneNode():
                print("\nSole survivor: ", people)

         #7. Advance to the next line
        line = in_file.readline()

main()
