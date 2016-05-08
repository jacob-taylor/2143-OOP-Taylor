# Jacob Taylor
# 5/7/2016
# Poker Game
# Problem: Create poker game based on rules given

import random
import operator
import os
from collections import Counter

#Card Class
#Holds Suit and Face values
class Card(object):

   #Taken from github repo
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    suits_symbols = ['♣', '♦', '♥', '♠']
    rank_names = [None, '2', '3', '4', '5', '6', '7','8', '9', '10', 'J', 'Q', 'K', 'A']

    #Constructor
    def __init__(self,s,f):
        self.suit = s
        self.faceVal = f

    def getSuit(self):
        return self.suit

    def getFaceVal(self):
        return self.faceVal

    def __str__(self):
        return '(%s,%s)' % (Card.rank_names[self.faceVal],Card.suit_names[self.suit])
    
    def __lt__(self, other):
        return self.faceVal > other.faceVal

#Deck class holds 52 cards
#Handles drawing cards and shuffling deck
class Deck(object):
    def __init__(self):
        self.deck = []
        self.shuffleDeck()

    #Draws 5 cards from deck and removes them from the deck so that they cannot be drawn again
    def drawHand(self):
        hand = []

        #Loops 5 times and appends a random card into the hand list
        #Also removes chosen card from deck to prevent redrawing the same card
        for i in range(5):
            cardIndex = random.randint(0,len(self.deck)-1)
            hand.append(self.deck[cardIndex])
            self.deck.remove(self.deck[cardIndex])   
        
        #sorts hand in descending order
        hand.sort()

        return hand

    #Draws 1 card from deck and removes it
    def getReDraw(self):
        cardIndex = random.randint(0,len(self.deck)-1)
        card = (self.deck[cardIndex])
        self.deck.remove(self.deck[cardIndex])
        return card 
    
    #Creates a new deck of cards
    def shuffleDeck(self):
        self.deck = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.deck.append(card)

class Poker(object):
    def __init__(self):

        #Variables to hold cards
        self.deck = Deck()
        self.hand = []

        #Variables to perform hand calculations
        self.pair = False
        self.twoPair = False
        self.threeKind = False
        self.fourKind = False
        self.fourSevens = False
        self.fourAces = False
        self.fourEights = False
        self.straight = False
        self.flush = False
        self.royal = False
        self.score = 0

    #Draws the first hand out of the deck
    #Shuffles the deck first to create a more random chance. 
    #Then pulls 5 random cards out of the list of cards and sets the hand
    def firstHand(self):
        self.deck.shuffleDeck()
        self.hand = self.deck.drawHand()
    
    #Draws new cards from the deck and keeps cards selected to be held to create a new hand.
    #Creates new hand and sorts it
    def reDraw(self,oldCards):
        temp = []
        amount = 0
        
        if oldCards != "None":
            kp = [int(x) for x in oldCards.split(',')]
            amount = len(kp)
            for i in range(amount):
                temp.append(self.hand[kp[i]])

        for i in range(5 - amount):
            temp.append(self.deck.getReDraw())
        
        self.hand = temp
        self.hand.sort()

    #Displays current hand and score
    def outputHand(self):
        for i in self.hand:
            print (i)
        print ('\nScore : %d' % (self.score))

    #Determines what kind of hand the user has and updates the score accordingly
    def calcHand(self):
        self.checkPairKind()
        self.checkFlush()
        self.checkRoyal()
        self.checkStraight()

        if(self.straight and self.flush and self.royal):
            print("Royal Flush : 800pts")
            self.score+=800
        elif(self.straight and self.flush):
            print("Straight Flush : 50pts")
            self.score+=50
        elif(self.flush):
            print("Flush : 5pts")
            self.score+=5
        elif(self.fourAces or self.fourEights):
            print("Four Aces or Eights : 80pts")
            self.score+=80
        elif(self.fourSevens):
            print("Four Sevens : 50pts")
            self.score+=50
        elif(self.fourKind):
            print("Four of a Kind : 25pts")
            self.score+=25
        elif(self.threeKind and self.pair):
            print("Full House : 8 pts")
            self.score+=8
        elif(self.threeKind):
            print("Three of a Kind : 3 pts")
            self.score+=3
        elif(self.twoPair):
            print("Two Pair : 2 pts")
            self.score+=2
        elif(self.pair):
            print("Pair : 1 pt")
            self.score+=2
        else:
            print("High Card : 0pts")

        self.resetHandBools()


    #Used to check for all combinations of Kinds and Pairs
    #Sets bool hand (see constructor) values to True if proper hand conditions are met
    def checkPairKind(self):
        kinds = []

        pairs = 0
        threeKind = 0
        fourKind = 0
        fourAces = 0
        fourSevens = 0
        fourEights = 0

        #Takes the faceVals of every card and puts them into a list
        for i in range(len(self.hand)):
            kinds.append(self.hand[i].getFaceVal())

        #List is converted into a counter
        p = Counter(kinds)
        for i in p:
            if p[i] == 2:
                pairs+=1
            elif p[i] == 3:
                threeKind+=1
            elif p[i] == 4:
                if i == 7:
                    fourSevens+=1
                elif i == 8:
                    fourEights+=1
                elif i == 13:
                    fourAces+=1
                else:
                    fourKind+=1

        if pairs == 1:
            self.pair = True
        if pairs == 2:
            self.twoPair = True
        if threeKind == 1:
            self.threeKind = True
        if fourKind == 1:
            self.fourKind = True
        elif fourSevens == 1:
            self.fourSevens = True
        elif fourAces == 1:
            self.fourAces = True
        elif fourEights == 1:
            self.fourEights = True

    #Checks if there is a flush
    def checkFlush(self):
        flush = True
        suit = self.hand[0].getSuit()
        
        for i in range(len(self.hand)):
            if suit != self.hand[i].getSuit():
                flush = False

        self.flush = flush

    #Checks if there is a straight
    def checkStraight(self):
        straight = False

        if((self.hand[0].getFaceVal() - 1) == self.hand[1].getFaceVal() 
           and (self.hand[1].getFaceVal() - 1) == self.hand[2].getFaceVal() 
           and (self.hand[2].getFaceVal() - 1) == self.hand[3].getFaceVal() 
           and (self.hand[3].getFaceVal() - 1) == self.hand[4].getFaceVal()):
               
            straight = True

        self.straight = straight

    #Checks if there is a royal flush
    def checkRoyal(self):
        if((self.hand[0].getFaceVal() == 13 )
           and (self.hand[1].getFaceVal() == 12)
           and (self.hand[2].getFaceVal() == 11)
           and (self.hand[3].getFaceVal() == 10)
           and (self.hand[4].getFaceVal() == 9)):
            
            self.royal = True
               

    #Resets values for next round
    def resetHandBools(self):
        self.pair = False
        self.twoPair = False
        self.threeKind = False
        self.fourKind = False
        self.fourSevens = False
        self.fourAces = False
        self.fourEights = False
        self.straight = False
        self.flush = False
        self.royal = False

    def resetScore(self):
        self.score = 0
       

another = True
Game = Poker()

#Loops until user is done playing
while another == True: 
    
    Game.firstHand()
              
    print ("\n---This is your hand------")
    Game.outputHand()
    print ("----------------------------\n")
    
    drawNew = input('Would you like to draw new cards?(Y/N): ')
    
    if drawNew == 'Y':
        keep = input('Enter the cards to hold. ex(0,2,3) Type None for completely new hand : ')
        Game.reDraw(keep)
    elif drawNew == 'N':
        print ("Your hand will now be evaluated.")
    else:
        print ("You should have typed Y!")

    os.system('cls')

    Game.calcHand()

    print ("\n---This is your hand---")
    Game.outputHand()
    print ("-----------------------------\n")

    more = input('Would you like to play another round?(Y/N): ')

    if more == 'Y':
        another = True
    elif more == 'N':
        another = False
        Game.resetScore()
    else:
        another = False
        Game.resetScore()
    os.system('cls')
    
    
    


