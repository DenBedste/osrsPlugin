import requests
import copy
from bs4 import BeautifulSoup

def experience(skill):
    string = title[title.find(skill) + 8:title.find(skill) + 30].splitlines()
    return string[0]

print("Enter RSN: ")

rsn = input()

URL="https://secure.runescape.com/m=hiscore_oldschool/hiscorepersonal?user1=" + rsn

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="contentHiscores")
title2 = title.find_all('td')
skills = ['Attack', 'Strength', 'Defence', 'Ranged', 'Prayer', 'Magic', 'Runecraft', 'Construction', 'Hitpoints', 'Agility', 'Herblore', 'Thieving', 'Crafting', 'Fletching', 'Slayer', 'Hunter', 'Mining', 'Smithing', 'Fishing', 'Cooking', 'Firemaking', 'Woodcutting', 'Farming']
titlelist = []
for titles in title2[0:]:
    titlelist.append(titles.text.strip())

newlist = list(filter(lambda a: a != "", titlelist))

for index, x in enumerate(newlist):
    print(skills[index])
    print(newlist[newlist.index(skills[index])+2 if skills[index] in newlist else 0])

#while(True):
    #print("\nEnter skill")
    #userInput = input()
    #print("\n")
    #value = newlist[newlist.index(userInput.capitalize())+2 if userInput.capitalize() in newlist else 0] if userInput.capitalize() in skills else "Not a skill \n try again"
    #if value == "Personal scores for " + rsn:
        #print("Not high enough try again")
    #else:
        #print(value)


exp = []

class Levels:
    
    def __init__(self, attack):
        for x in skills:
            exp.append(experience(x))
        

    def showLevels(self):
        for i, x in enumerate(exp):
            print(skills[x])
            print(exp[x])



#hiscore = Levels('huez')

#hiscore.showLevels()

#print("Enter skill")

#skill = input().capitalize()

#print(experience(skill))
