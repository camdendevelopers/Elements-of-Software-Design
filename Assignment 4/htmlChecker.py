#  File: htmlChecker.py
#  Description: This program analyzes HTML code and checks for inconsistencies
#  Student's Name: Marcos Ortiz
#  Student's UT EID: mjo579
#  Course Name: CS 313E
#  Unique Number: 51320
#
#  Date Created: 10/3/2016
#  Date Last Modified: 10/6/2016

class Stack (object):

   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def push (self, item):
      self.items.append (item)

   def pop (self):
      return self.items.pop ()

   def peek (self):
      return self.items[-1]

   def size (self):
      return len(self.items)

   def show(self):
       return self.items

def getTag(f):
    tag = ""
    ch = f.read(1)

    while ch != "<":
        if ch == "":
            return tag
        ch = f.read(1)

    ch = f.read(1)
    while ch != ">" and (not ch.isspace()):
        tag += ch
        ch = f.read(1)
    return tag

def createTags():
    #Create file from text
    in_file = open("./htmlfile.txt", "r")
    tags = []
    tag = getTag(in_file)
    while tag != "":
        tags.append(tag)
        tag = getTag(in_file)
    return(tags)

def printGrid (numsPerRow, l):
    copyL = l[:]
    numsInRow = 1
    for i in range(len(l)):
        if numsInRow % numsPerRow == 0:
            copyL[i] = copyL[i] + "\n"
            numsInRow = 1
        else:
            copyL[i] = copyL[i] + "\t"
            numsInRow += 1
    return copyL

def main():
    stack = Stack()
    tags = createTags()
    EXCEPTIONS = ["area", "base", "br", "col", "command", "embed", "hr", "img", "input", "link", "meta", "param", "source"]
    VALIDTAGS = []

    #print("Tags found in file: \n{}\n".format(tags))
    print("\nTags found in file:")
    print ("".join(printGrid(8, tags)))
    print()

    for tag in tags:
        if tag[0] != "/" and tag in EXCEPTIONS:
            print("Tag {} does not need to match:  stack is still {}".format(tag, stack.items))
        elif tag[0] != "/":
            if not tag in VALIDTAGS:
                print("Tag {} not recognized but added to valid tags".format(tag))
                VALIDTAGS.append(tag)
            stack.push(tag)
            print("Tag {} pushed:  stack is now {}".format(tag, stack.items))
            input("paused\n")
        elif tag[1:] == stack.peek():
            stack.pop()
            print("Tag {} matches top of stack:  stack is now {}\n".format(tag, stack.items))
        else:
            print("Error:  tag is {} but top of stack is {}\n".format(tag, stack.peek()))
            break

    if stack.isEmpty():
        print("Processing complete.  No mismatches found.\n")
    else:
        print("Processing complete.  Unmatched tags remain on stack: {}\n".format(stack.items))

    VALIDTAGS.sort()
    print("Valid tags found: {}\n".format(VALIDTAGS))
    print("List of exceptions: {}\n".format(EXCEPTIONS))
main()
