import pandas ## better than the csv module
from random import choice

unbiased = 1
man_name = 0  
woman_name = 0

columnNames_1=['year', 'name', 'percent', 'sex']
columnNames_2=['name', 'rank', 'count', 'prop100k', 'cum_prop100k', 'pctwhite', 'pctblack', 'pctapi', 'pctaian', 'pct2prace', 'pcthispanic']

fnData = pandas.read_csv('baby-names.csv', names = columnNames_1)
firstName = fnData.name.tolist()
sexList = fnData.sex.tolist()

man = []
woman = []
for x in range(1,len(sexList)):
    if sexList[x]=="boy":
        man.append(firstName[x])

for x in range(1,len(sexList)):
    if sexList[x]=="girl":
        woman.append(firstName[x])



lnData = pandas.read_csv('surnames.csv', names = columnNames_2)
lastName = lnData.name.tolist()


stop = 0
while stop != 1:
    if unbiased == 1:
        print (choice(firstName) + " " + choice(lastName))
    if man_name == 1:
        print (choice(man) + " " + choice(lastName))
    if woman_name == 1:
        print (choice(woman) + " " + choice(lastName))
    stop=input()
    






