'''
Project 1: Make a dictionary!
How it works?
User enters a word, and we fetch its meaning from the json file. If the word is there, we get the meaning. Otherwise we check for similar words and then prompt the user.
    For eg: User enters Rainnn
    Out: Did you mean "Rain"?

Libraries Used:
    json
    difflib - get_close_matches
    and lots of awesomeness!

Future things to do? -
    Will connect it to a live database and query.
'''

import json
from difflib import get_close_matches

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        ans = input("Did you mean %s instead? Enter Y/N \n" % get_close_matches(word, data.keys())[0])
        if ans.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif ans.lower() == "n":
            return "Word does not exist, please check later!"
        else:
            return "We didnt understand your query :P"
    else:
        return "Please enter a valid word"

data = json.load(open("data.json", 'r'))
word = input("Enter word: ")
out = (translate(word))

if type(out) == list:
    for item in out:
        print(item)
else:
    print(out)
