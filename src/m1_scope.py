###############################################################################
# TODO: 1. (9 pts)
#
#   For this _todo_, reference the code below.
#
#   At each location below, indicate the values of each of these variables:
#
#       a
#       m
#       self.a
#       self.m
#       t1.a
#       t1.m
#       t2.a
#       t2.m
#
#   I have provided a comment below the code where you can indicate the values
#   of each object. If a variable is undefined, simply put an  X  .
#
#   Feel free to include some print statements to help you with this problem if
#   you think it would be helpful.
#
#   I will do one of these in class so you know how I would like you to
#   indicate your answers.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

a = 20

class Tiny():
    def __init__(self, a):
        ### Location 1
        self.a = 5
        self.m = a + 3
        ### Location 2

def foo(a):
    ### Location 3
    a = 7
    m = 25
    a += 2
    a = a + m
    ### Location 4
    t1 = Tiny(10)
    t2 = Tiny(12)
    t1.m = t1.m + t2.m
    ### Location 5
    return t1.m


def bar(a):
    ### Location 6
    m = 1
    a = a + m
    m = 3
    ### Location 7
    return a

def main():
    ### Location 8
    a = foo(a)
    m = bar(a)
    ### Location 9

main()

###############################################################################
# 
#   Location 1          Location 2          Location 3
#   a = 34              a = 34              a = 20              
#   m = 25              m = X               m = X              
#   self.a = X          self.a = 5          self.a = X         
#   self.m = X          self.m = 37         self.m = X         
#   t1.a = X            t1.a = X            t1.a = X           
#   t1.m = X            t1.m = X            t1.m = X           
#   t2.a = X            t2.a = X            t2.a = X           
#   t2.m = X            t2.m = X            t2.m = X           
#
#   Location 4          Location 5          Location 6
#   a = 34              a = 34              a = 28             
#   m = 25              m = 25              m = X             
#   self.a              self.a = X          self.a = X        
#   self.m              self.m = X          self.m = X        
#   t1.a = X            t1.a = 5            t1.a = X       
#   t1.m = X            t1.m = 28           t1.m = X         
#   t2.a =X             t2.a = 5            t2.a = X         
#   t2.m = X            t2.m = 15           t2.m = X         
#
#   Location 7          Location 8          Location 9
#   a = 29              a = 20              a = 29               
#   m = 3               m = X               m = 29              
#   self.a = X          self.a = X          self.a = X         
#   self.m = X          self.m = X          self.m = X        
#   t1.a = X            t1.a = X            t1.a = X           
#   t1.m = X            t1.m = X            t1.m = X           
#   t2.a = X            t2.a = X            t2.a = X           
#   t2.m = X             t2.m = X            t2.m = X           
#
###############################################################################
 
 #834125679