import json
import difflib
from difflib  import SequenceMatcher
data = json.load(open('data.json'))

def translate(keyword):
    keyword = keyword.lower()
    if keyword in data:
        return data[keyword]
    else:
        return "Sorry!! I do not have this word in my memory"

input_keyword = input("Enter a word : ")

print(translate(input_keyword))