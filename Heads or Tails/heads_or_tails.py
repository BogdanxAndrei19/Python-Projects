from random import choice

stop = 0
while stop!=1:
    print ("Flip a coin?")
    ans = input()
    assert (ans == 'yes' or ans == 'no'), "Input should be only yes or no"
    if ans == 'yes':
        print(choice(['heads','tails']))
    if ans == 'no':
        stop = 1
    
