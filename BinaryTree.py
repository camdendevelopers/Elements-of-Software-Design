# Using linked listed
# ---------------------------
# |          data            |
# | left node  | right node  |
# ----------------------------
#

class BinaryTree:
    def __init__(self, initdata):
        self.data = initdata
        self.left = None
        self.right = None

    def getRootVal(self):
        return self.data

    def setRootVal(self, value):
        self.data = value

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def insertLeft(self, newValue):
        temp = self.getLeftChild()
        new = BinaryTree(newValue)
        self.left = new
        new.left = temp

    def insertRight(self, newValue):
        temp = self.getRightChild()
        new = BinaryTree(newValue)
        self.right = new
        new.right = temp
'''
######################################
#Python tree implementation
def BinaryTree(initdata):
   return [ initdata, [], [] ]

def getRootVal(root):
   return root[0]

def setRootVal(root, newVal):
   root[0] = newVal

def getLeftChild(root):
   return root[1]

def getRightChild(root):
   return root[2]

def insertLeft(root,newBranch):
   t = root.pop(1)                       # temporarily break the tree
   if len(t) > 1:                        # if something already
      root.insert(1,[newBranch,t,[] ] )  # there, push it down as
   else:                                 # the new left child
      root.insert(1,[newBranch,[],[] ] )

def insertRight(root,newBranch):
   t = root.pop(2)
   if len(t) > 1:                        # if something already
      root.insert(2,[newBranch,[],t ] )  # there, push it down as
   else:                                 # the new right child
      root.insert(2,[newBranch,[],[] ] )

'''
#           3
#       5       7
#     4   8   9   6

# To display the tree, use preorder (prefix)
# 1. Visit a node R, print the value of that node first
# 2. Then travel to the left tree and recurse
# 3. Then travel to the right tree and recurse
# 3, 5, 4, 8, 7, 9, 6

# To display the tree, use postorder (prefix)
# 1. Then travel to the left tree and recurse
# 2. Then travel to the right tree and recurse
# 3. Visit a node R, print the value of that node first
# 4, 8, 5, 9, 6, 7, 3

# To display the tree, use inorder (prefix)
# 1. Then travel to the left tree and recurse
# 2. Visit a node R, print the value of that node first
# 3. Then travel to the right tree and recurse
# 4, 5, 8, 3, 9, 7, 6

# Using python list implementation
def preorder(tree):
    if tree != []:
        print(getRootVal(tree))
        preorder(getLeftChild(tree))
        preorder(getRightChild(tree))

def postorder(tree):
    if tree != []:
        preorder(getLeftChild(tree))
        preorder(getRightChild(tree))
        print(getRootVal(tree))

def inorder(tree):
    if tree != []:
        preorder(getLeftChild(tree))
        print(getRootVal(tree))
        preorder(getRightChild(tree))
