#  File: ExpressionTree.py
#  Description: This program performs creates a tree from a given expression and computes the answer
#  Student's Name: Marcos Ortiz
#  Student's UT EID: mjo579
#  Course Name: CS 313E
#  Unique Number: 51320
#
#  Date Created: 11/28/2016
#  Date Last Modified: 12/02/2016

import time
import sys
sys.setrecursionlimit(10000)

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
      return self.items [len(self.items)-1]

   def size (self):
      return len(self.items)

class BinaryTree (object):
    def __init__(self, initdata = "root"):
      self.data = initdata
      self.left = None
      self.right = None
      self.stack = Stack()
      self.postorderString = ""
      self.inorderString = ""
      self.inorderCalculation = 0
      self.preorderString = ""

    def insertLeft(self,newNode):
      if self.left == None:
         self.left = BinaryTree(newNode)
      else:
         t = BinaryTree(newNode)
         t.left = self.left
         self.left = t

    def insertRight(self,newNode):
      if self.right == None:
         self.right = BinaryTree(newNode)
      else:
         t = BinaryTree(newNode)
         t.right = self.right
         self.right = t

    def getLeftChild(self):
      return self.left

    def getRightChild(self):
      return self.right

    def setRootVal(self,value):
      self.data = value

    def getRootVal(self):
      return self.data

    def createTree (self, expr):
        operatorList = ['+', '-', '*', '/']
        currentNode = self
        stack = Stack()

        for index in range(0, len(expr)-1):
            currentToken = expr[index]

            if currentToken == ")":
                currentNode = stack.pop()

            elif currentToken == "(":
                stack.push(currentNode)
                currentNode.insertLeft(currentToken)
                currentNode = currentNode.getLeftChild()

            elif currentToken in operatorList:
                currentNode.setRootVal(currentToken)
                currentNode.insertRight(currentToken)
                stack.push(currentNode)
                currentNode = currentNode.getRightChild()

            else:
                currentNode.setRootVal(currentToken)
                currentNode = stack.pop()

    def evaluate (self, root):
        operatorList = ['+', '-', '*', '/']

        if root != None:
            self.evaluate(root.getLeftChild())
            self.evaluate(root.getRightChild())

            element = root.getRootVal()

            if element in operatorList:
                num1 = self.stack.pop()
                num2 = self.stack.pop()

                if element == "+":
                    answer = num2 + num1
                elif element == "-":
                    answer = num2 - num1
                elif element == "*":
                    answer = num2 * num1
                else:
                    answer = num2 / num1

                self.stack.push(answer)
                self.inorderCalculation = answer

            else:
                self.stack.push(eval(element))

        return self.inorderCalculation

    def preorder (self, root):
        if root != None:
            self.preorderString += root.getRootVal() + " "
            self.preorder(root.getLeftChild())
            self.preorder(root.getRightChild())

        return self.preorderString

    def postorder (self, root):
        if root != None:
            self.postorder(root.getLeftChild())
            self.postorder(root.getRightChild())
            self.postorderString += root.getRootVal() + " "

        return self.postorderString

def main():

    # 1. Open file and read data
    in_file = open("treedata.txt", "r")

    # 2. Read file line by line
    for line in in_file:

        # 3. Perform line specific tasks
        line = line.strip()
        print("Infix expression: ", line)
        line = line.split()

        # 4. Instantiate tree and create it
        tree = BinaryTree()
        tree.createTree(line)

        # 5. Print results
        print("\tValue:   ", tree.evaluate(tree))
        print("\tPrefix expression: ", tree.preorder(tree))
        print("\tPostfix expression: ", tree.postorder(tree))
        print()

main()
