#! python2
##dice roller
import random
import sys
import time

print (sys.version)
time.sleep(7)
minim=1
maxim=6
stop=0

print("Let's roll a dice")

while (stop==0):
    print(random.randrange(minim,maxim))
    print ("Roll Again?")
    ans=input()
    if ans==0:
        stop=1
        print("Game over!")

        

        
