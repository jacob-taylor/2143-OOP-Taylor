"""
    Jacob Taylor
    Game Of Life
    2/3/2016

    HomeWork 2 - Implement liveOrdie to return 1 or 0 depending on if the cell being tested is going to live or die
    Done - 2/2/2016
"""
import time
import os
import random
import platform

class golBoard(object):
    """
    Game fully implemented using code provided in class. 
    I Added one function checkNeighbor to be used in liveOrdie.
    An introduction to python using the game of life as a problem to solve in class.
    Not the most pythonic or succinct solution, but it's not meant to be.
    Any live cell with fewer than two live neighbours dies, as if caused by under-population.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by over-population.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """
    def __init__(self,rows=20,cols=20,populate=False,Density=.25):
        random.seed()
        self.width = cols
        self.height = rows

        if populate:
            self.currentGen = self.initRandGen(Density)
        else:
            self.currentGen = self.initGen()

    def initGen(self):
        """
        @function: initGen
        @description: Initializes a single generation 
        @param: None
        @returns: list - 2D list containing 0's
        """     
     
        board =[[0 for x in range(self.width)] for y in range(self.height)]
        return board
    
    
       
    def initRandGen(self,density):
        """
        @function: initRandGen
        @description: Initializes a random generation 
        @param: float - density (how many lives to create)
        @returns: list - 2D list containing 0 and 1
        """     
        gen = self.initGen()

        
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in gen]))
        
        numberOfLives = int(self.width * self.height * density)
        
        for i in range(numberOfLives):
                row = random.randint(0, self.height-1)
                col = random.randint(0, self.width-1)
                gen[row][col] = self.randomLife()       
        return gen
        

    def randomLife(self):
        """
        @function: randomLife
        @description: Generates a random life (zero or one)
        @param: none
        @returns: bool - zero or one (alive or dead)
        """    
        if random.random() > .5:
            x = 1
        else:
            x = 0
        return x

    def computeNextGen(self):
        """
        @function: computeNextGen
        @description: Computes the next generation our cellular automata 
        @param: None
        @returns: None
        """     
        nextGen = self.initGen()
        for row in range(self.height):
            for col in range(self.width):
                nextGen[row][col] = self.liveOrDie(row,col)
        self.currentGen = nextGen

    def liveOrDie(self,r,c):
        """
        @function: liveOrDie
        @description: Calculates whether a cell lives or dies based on Game of Life rules
        @param: int x - Column to check
        @param: int y - Row to check
        @returns: Int:1 is returned if the cell will live or 0 if the cell is going to die
        """  
        #Gets the cellls status i.e. Alive or Dead(1/0)
        status = (self.currentGen[r][c])
        count = 0

        #Checks every possible neighbor if the neighbors is out of bounds 0 is returned
        count += self.checkNeighbor(r-1,c-1)
        count += self.checkNeighbor(r-1,c+1)
        count += self.checkNeighbor(r-1,c)
        count += self.checkNeighbor(r+1,c-1)
        count += self.checkNeighbor(r+1,c+1)
        count += self.checkNeighbor(r+1,c)
        count += self.checkNeighbor(r,c-1)
        count += self.checkNeighbor(r,c+1)

        #Determines if the cell will live or die based on the rules of the game
        if(status):
            if count < 2 or count > 3:
                return 0 
            else:
                return 1
        else:
            if count == 3:
                return 1
            else:
                return 0 


    def checkNeighbor(self,r,c):
        """
        @function: checkNeighbor
        @description: determines wether a cell is in the bounds of the board and if it is alive or dead
        @param: int r - Row to check
        @param: int c - Column to check
        @returns: Int: if the cell is within bounds a 1 or 0 is returned depending on if the cell is alive or dead  
        """  
        #If the cell is within the bounds of the board the cell's status is returned and added to count
        if( r>=0 and c>=0 and r<self.height and c<self.width):
            if(self.currentGen[r][c]==0):
                return 0
            elif(self.currentGen[r][c] == 1):
                return 1
        else:
            return 0


    def printBoard(self):
        """
        @function: printBoard
        @description: Prints the current board
        @param: none
        @returns: output
        """
        print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in self.currentGen]))


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: "))
generations = int(input("Enter the number of generations you wish to see: "))
density = float(input("Enter the intial denstiy of live cells: "))
sleep = float(input("Enter the amount of delay between prints: "))
b = golBoard(rows,cols,True,density)
     
for x in range(generations):
    os.system('cls')
    print "Generation %s\n" % (x+1)
    b.printBoard()
    b.computeNextGen()
    time.sleep(sleep)
    
print "\n"