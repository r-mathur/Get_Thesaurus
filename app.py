import json
from difflib import get_close_matches
data = json.load(open('data.json'))

def translate(keyword):
    keyword = keyword.lower()

    if keyword in data:
        return data[keyword]

    elif len(get_close_matches(keyword, data.keys(), cutoff=0.72)) > 0 :

        choice = input("Did you mean %s instead? [Yes(Y)/No(N)]: " % get_close_matches(keyword, data.keys())[0])

        if choice.lower() =='yes' or choice.lower() == 'y':
            return data[get_close_matches(keyword, data.keys())[0]]

        elif choice.lower() == 'no' or choice.lower() == 'n':
            return "Sorry the word doesn't exist in my dictionary. Please check it."

        else:
            return "I didn't understand your entry"

    else:
        return "Sorry!! I do not have this word in my memory"

input_keyword = input("Enter a word : ")

result = translate(input_keyword)

if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)