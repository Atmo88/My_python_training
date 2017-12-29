import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif get_close_matches(word, data.keys()):
        corrected = get_close_matches(word, data.keys())[0]
        toCorrect = input("Did you mean %s instead? Enter Y if yes, N if no: " % corrected)
        if toCorrect in ["y", "Y"]:
            return data[corrected]
        elif toCorrect in ["n", "N"]:
            return "This word doesn't exist, please double check it"
        else:
            return "Sorry, we didn't understand your entry."
    else:
        return "This word doesn't exist, please double check it"

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
