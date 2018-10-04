import requests
import argparse
from strings import *

def printRecipes(data):
  for key in data['hits'][int(option)-1]['recipe']['ingredients']:
    print key['text']

parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument('-c', '--calories', help='Show calories', required=False,
action='store_true')
parser.add_argument('-d', '--detailed-calories', help='Show detailed' + 
' nutritional content', required=False, action='store_true')

args = parser.parse_args()

appid = 'ea7c9913'
appkey = '8c999d827f6d9b69c8892f47e2bc5cd3'

searchQuery = raw_input(USER_PROMPT)

r = requests.get('https://api.edamam.com/search?q=' + searchQuery + '&app_id='
   + appid + '&app_key=' + appkey)

data = r.json()

i = 1
l1 = []
for key in data['hits']: # print titles of recipes
  l1.insert(i-1, key['recipe']['label'])
  print(str(i) + ') '+ key['recipe']['label'])
  i += 1


option = raw_input(USER_SELECT)
print(l1[int(option)-1])

if not args.calories: # print recipe ingredients only
  printRecipes(data)

elif(args.calories): # print recipe ingredients and calories
  printRecipes(data)
  print "Calories: " + str(data['hits'][int(option)-1]['recipe']['calories'])

if args.detailed_calories: # print recipe ingredients and nutritional info
  printRecipes(data)
  for key in data['hits'][int(option)-1]['recipe']['digest']:
    print key['label'] + " " + str(key['total']) + key['unit']

