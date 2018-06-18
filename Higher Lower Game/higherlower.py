import pandas
from random import choice, randint

columnNames = ['search','number_of_searches']
search_registry = pandas.read_csv('data.csv', names = columnNames)

keywords = search_registry.search.tolist()
values = search_registry.number_of_searches.tolist()

points = 0
stop = 0

while stop != 1:
    
    randomIndex_1 = randint(1,len(keywords)-1)
    print ( keywords[randomIndex_1] + " has {} monthly global searches ".format(values[randomIndex_1]) )
        
    randomIndex_2 = choice([i for i in range(1,len(keywords)) if i != randomIndex_1])
    print ( "How many does {} have? Higher or Lower?".format(keywords[randomIndex_2]))
    
    ans = input()
    assert (ans == 'higher' or ans=='lower'), "Please type only higher or lower"
    
    if ans == 'higher':
        if int(values[randomIndex_1]) < int(values[randomIndex_2]):
            points+=1
        else:
            print("GAME OVER. You got {} points".format(points))
            stop=1
            
    if ans == 'lower':
        if int(values[randomIndex_1]) > int(values[randomIndex_2]):
            points+=1
        else:
            print("GAME OVER. You got {} points".format(points))
            stop=1



