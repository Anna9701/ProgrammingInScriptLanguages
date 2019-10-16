import re

def get_anagrams (list_of_words):
    anagrams_dictionary = {}

    for word in list_of_words:
        characters = sorted(word)
        characters = "".join(characters)
        if characters in anagrams_dictionary:
            anagrams_dictionary[characters].append(word)
        else:
            anagrams_dictionary[characters] = [word]

    return anagrams_dictionary

non_letter_regex = re.compile('[^a-zA-Z\s]')

file = open("english.50MB", "r")
text = file.read().lower()
file.close()

filtered_text = non_letter_regex.sub('', text)

words = filtered_text.split()
numberOfWords = len(words)
setOfWords = set(words)
numberOfWordsInSet = len(setOfWords)

print("Number of words")
print(numberOfWords)
print("Number of unique words")
print(numberOfWordsInSet)

print(words[:100])

words = [word for word in words if len(word) > 1]
print("Number of words with length > 1")
print(len(words))
setOfWords = set(words)
print("Number of unique words with length > 1")
print(len(setOfWords))

palindromes = [word for word in setOfWords if str(word) == str(word)[::-1]]
print("Number of palindromes")
print(len(palindromes))
print(palindromes[:100])

dictionary = get_anagrams(setOfWords)
count = 0
for key, val in dictionary.items():
    if len(val) > 1:
        count += 1

print("Anagrams count")
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

print("Number of pairs")
print(numberOfWords)
print("Number of unique pairs")
print(numberOfWordsInSet)

palindromes = [word for word in setOfWords if str(word) == str(word)[::-1]]
print("Number of palindromes")
print(len(palindromes))
print(palindromes[:100])

dictionary = get_anagrams(setOfWords)
count = 0
for key, val in dictionary.items():
    if len(val) > 1:
        count += 1

print("Number of anagrams")
print(count)
print(dictionary[:20])