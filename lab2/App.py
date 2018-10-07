import sys

class Node:
    def __init__(self):
        self.c = None
        self.m = None
        self.side = None
        self.childNodes = []
        self.parentNode = None
        self.move = 0

    def giveVariables (self, c, m, side, move = 0):
        self.c = c
        self.m = m
        self.side = side
        self.move = move

    def giveParent(self, node):
        self.parentNode = node

    def addChildren (self, children):
        for child in children:
            self.childNodes.append(child)

    def showYourSelf(self, p = ""):
        print(p, "C:", self.c, ", M:", self.m, ", Side:", self.side, ", Moves:", self.move, end="", sep="")
        if (len(self.childNodes) != 0):
            print()
        for child in self.childNodes:
            child.showYourSelf(p= p + "|    ")
        print()

def main():
    sys.setrecursionlimit(10000)
    initNode = Node()
    initNode.giveVariables(3, 3, True)

    searchTree(initNode)

    initNode.showYourSelf()

def searchTree(node):
    findNodes(node)
    #print("\n\n\n")
    #node.showYourSelf()
    if (len(node.childNodes) != 0):
        for child in node.childNodes:
            searchTree(child)

def findNodes(node):
    if (node.c is 0 and node.m is 0 and node.side is False):
        return

    temp_c = node.c
    temp_m = node.m

    if (node.side == False):
        temp_c = 3 - node.c
        temp_m = 3 - node.m

    # 2 people
    if (temp_c > 1):
        newnode = Node()
        if (node.side):
            newnode.giveVariables(node.c - 2, node.m, not node.side, move=node.move + 1)
        else:
            newnode.giveVariables(node.c + 2, node.m, not node.side, move=node.move + 1)
        newnode.parentNode = node
        if (isItPossible(newnode)):
            node.addChildren([newnode])

    if (temp_m > 0 and temp_c > 0):
        newnode = Node()
        if (node.side):
            newnode.giveVariables(node.c - 1, node.m - 1, not node.side, move=node.move + 1)
        else:
            newnode.giveVariables(node.c + 1, node.m + 1, not node.side, move=node.move + 1)
        newnode.parentNode = node
        if (isItPossible(newnode)):
            node.addChildren([newnode])

    if (temp_m > 1):
        newnode = Node()
        if (node.side):
            newnode.giveVariables(node.c, node.m - 2, not node.side, move=node.move + 1)
        else:
            newnode.giveVariables(node.c, node.m + 2, not node.side, move=node.move + 1)
        newnode.parentNode = node
        if (isItPossible(newnode)):
            node.addChildren([newnode])
    # 1 person
    if (temp_m > 0):
        newnode = Node()
        if (node.side):
            newnode.giveVariables(node.c, node.m - 1, not node.side, move=node.move + 1)
        else:
            newnode.giveVariables(node.c, node.m + 1, not node.side, move=node.move + 1)
        newnode.parentNode = node
        if (isItPossible(newnode)):
            node.addChildren([newnode])

    if (temp_c > 0):
        newnode = Node()
        if (node.side):
            newnode.giveVariables(node.c - 1, node.m, not node.side, move=node.move + 1)
        else:
            newnode.giveVariables(node.c + 1, node.m, not node.side, move=node.move + 1)
        newnode.parentNode = node
        if (isItPossible(newnode)):
            node.addChildren([newnode])

def isItPossible(node):
    if (node.m == 0):
        leftside = 1
    else:
        leftside = node.m - node.c

    if ((3 - node.m) == 0):
        rightside = 1
    else:
        rightside = (3 - node.m) - (3 - node.c)


    if (node.parentNode is not None):
        if (node.parentNode.parentNode is not None):
            if (node.parentNode.parentNode.c == node.c and node.parentNode.parentNode.m == node.m):
                return False

    if (node.c == 3 and node.m == 3 and node.side == True):
        return False

    if ((leftside < 0) or (rightside < 0)):
        return False
    return True

if __name__ == '__main__':
    main()