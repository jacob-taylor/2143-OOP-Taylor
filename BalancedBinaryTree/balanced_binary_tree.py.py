#Jacob Taylor
#
#Program 2 - Binary Tree Balanced Loading
#   Problem: Find a way to make a balanced binary search tree
#
# Starter Code porvided

import random

#Node class which holds all the information for a single node
#
#I chose to add this becasue it was easier for me to use recursion 
# in the actual BalancedSearch Class
# 
# right/left = children info
# data = data for node
class Node(object):
    def __init__(self,x):
        self.right = None
        self.left = None
        self.data = x

class BalancedSearch(object):
    def __init__(self):
        self.num = []
        self.preOut = []
    
    #Splits sorted list into a quasi-Sorted list that allows the creation of a balanced tree.
    def balanceList(self,list):
        if len(list) == 0:
            return
        else:
            self.num.append(list[len(list)//2])
            self.balanceList(list[:len(list)//2])
            self.balanceList(list[len(list)//2+1:])
    
    #Prints list of numbers used to generate tree
    def printList(self):
        print (self.nums)

    #Standard insert into binary search tree
    def insert(self,root, node):
        if root == None:
            root = node
        else:
            if root.data > node.data:
                if root.left == None:
                    root.left = node
                else:
                    self.insert(root.left, node)
            else:
                if root.right == None:
                    root.right = node
                else:
                    self.insert(root.right, node)

    #Generates a list based on a pre order traversal of a BST
    def setPreOrderList(self,root):
        if not root:
            return        
        self.preOut.append(root.data)
        self.setPreOrderList(root.left)
        self.setPreOrderList(root.right)   
    

unique = []

num = input('Enter te number of integers(1-100000) : ')
# loop 1000 times
for x in range(int(num)):

    # get a random number
    r = random.randint(0,100)

    # if it's not already in the list, enter it.
    if r not in unique:
        unique.append(r)

# Sort the list
unique.sort()

#Creates empty Binar Search Tree
BST = BalancedSearch()

#Creates list of random numbers to be used in creation of balanced tree
BST.balanceList(unique)

#Sets root node and removes it from the list of values
r = Node(BST.num[0])
BST.num.pop(0)

#Creates tree by inserting values one at a time.
for i in BST.num:
    BST.insert(r,Node(i))

#Generates a list based on a pre order traversal of a BST
BST.setPreOrderList(r)

#Prints "preOrdered" list
print(BST.preOut)



