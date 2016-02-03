"""
Jacob Taylor
2/2/2016

HomeWork 1

Add and addition method in the fraction class and 
create a reduced mixed fraction from the sum of two fraction
"""

from fractions import gcd

class fraction(object):
    def __init__(self,n=None,d=None,m=None):
        self.numerator = n
        self.denominator = d
        self.mixed = m

    def __str__(self):

        #returns the mixed fraction
        if(self.mixed != None):
            return "%s %s/%s" % (self.mixed, self.numerator , self.denominator)
        
        #returns non-mixed fraction
        return "%s/%s" % (self.numerator , self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)

    # Adds two fractions together and turns them into a reduced mixed fraction 
    def __add__(self,rhs):
        x = (self.numerator * rhs.denominator)+(rhs.numerator * self.denominator)
        y = self.denominator * rhs.denominator

        mix = x%y

        if(mix > 0):
            div = x/y;
            #uses gcd to reduce fraction
            reduce = gcd(mix,y)
            return fraction(mix/reduce,y/reduce,div)

        return fraction(x,y)

if __name__ == '__main__':
    
       
        #Loops until the user inputs something other than Y
        #Reads in 4 values for the numerators and the denominators
        #initializes a and b with entered values and adds them
        repeat = "Y"
        while repeat == "Y":
            num1 = input("Enter first numerator: ")
            den1 = input("Enter first denomenator: ")
            num2 = input("Enter second numerator: ")
            den2 = input("Enter second denominator: ")
    
            a = fraction(num1,den1)
            b = fraction(num2,den2)
            c = a + b
        
            print "\n%s + %s = %s" % (a,b,c)
            repeat = raw_input("\nWould you like to enter another set of fractions?(Y/N)")
            print "\n"