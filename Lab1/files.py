import re

def get_anagrams (listOfWords):
    anagramsDictionary = {}

    for word in listOfWords:
        characters = sorted(word)
        characters = "".join(characters)
        if characters in anagramsDictionary:
            anagramsDictionary[characters].append(word)
        else:
            anagramsDictionary[characters] = [word]

    return anagramsDictionary

regex = re.compile('[^a-zA-Z\s]')
#First parameter is the replacement, second parameter is your input string

file = open("english.50MB", "r")
text = file.read()
file.close()

text = text.lower()
x = regex.sub('', text)

words = x.split()
numberOfWords = len(words)

setOfWords = set(words)
numberOfWordsInSet = len(setOfWords)

print("Number of words")
print(numberOfWords)
print("Number of unique words")
print(numberOfWordsInSet)

print(words[:100])

words = [word for word in words if len(word) > 1]
print(len(words))
setOfWords = set(words)
print(len(setOfWords))

palindroms = [word for word in setOfWords if str(word) == str(word)[::-1]]
print(len(palindroms))
print(palindroms[:100])


# dictionary = {}
#
# for word in setOfWords:
#     chars = sorted(word)
#     chars = "".join(chars)
#     if chars in dictionary:
#         dictionary[chars].append(word)
#     else:
#         dictionary[chars] = [word]

dictionary = get_anagrams(setOfWords)
count = 0
for key, val in dictionary.items():
    if len(val) > 1:
        count += 1

print(count)

### Exercise 4
print("**************Exercise 4************************")
pairs = tuple((words[i], words[i+1]) for i in range(len(words)-1))
print(len(pairs))
pairsSet = set(pairs)
print(len(pairsSet))

words = []

for pair in pairsSet:
    words.append("".join(pair))

numberOfWords = len(words)

setOfWords = set(words)
numberOfWordsInSet = len(setOfWords)

print("Number of words")
print(numberOfWords)
print("Number of unique words")
print(numberOfWordsInSet)

palindroms = [word for word in setOfWords if str(word) == str(word)[::-1]]
print(len(palindroms))
print(palindroms[:100])

dictionary = get_anagrams(setOfWords)
count = 0
for key, val in dictionary.items():
    if len(val) > 1:
        count += 1

print(count)