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

# To display the tree, use preorder (prefix)
# 1. Visit a node R, print the value of that node first
# 2. Then travel to the left tree and recurse
# 3. Then travel to the right tree and recurse
# 5, 7, 3, 8, 1

# To display the tree, use postorder (prefix)
# 1. Then travel to the left tree and recurse
# 2. Then travel to the right tree and recurse
# 3. Visit a node R, print the value of that node first
# 8, 1, 3, 7, 5

# To display the tree, use inorder (prefix)
# 1. Then travel to the left tree and recurse
# 2. Visit a node R, print the value of that node first
# 3. Then travel to the right tree and recurse
# 5, 8, 3, 1, 7
