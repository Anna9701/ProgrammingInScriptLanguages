import random
from itertools import islice

def window(seq, n):
    """Returns a sliding window (of width n) over data from the iterable
       s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   """
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def get_min_hash(row, seed):
    #parts = [row[mi:mi+Q] for mi in range(0, len(row), Q)]
    parts = list(window(row, Q))
    min_hash = hash(parts[0]) ^ seed
    for part in parts:
        hash_value = hash(part) ^ seed
        if hash_value < min_hash:
            min_hash = hash_value
    return min_hash

def get_min_hashes(row):
    hashes = []
    for seed in seeds:
        hashes.append(get_min_hash(row, seed))
    return hashes

def are_texts_similar(first_hashes, second_hashes):
    equal_hashes = 0
    for ih in range(100):
        if first_hashes[ih] == second_hashes[ih]:
            equal_hashes += 1
    return equal_hashes >= 30

file = "sampletext.txt"
texts = open(file).read().split("\n")
texts = list(filter(None, texts))
Q = 15

seeds = []
for i in range (100):
    seeds.append(random.getrandbits(64))

print(seeds)
print(len(texts))

texts_hashes = list()
for i in range(len(texts)):
    texts_hashes.append(list())
for i in range(len(texts)):
    texts_hashes[i].append(get_min_hashes(texts[i]))
for i in range(len(texts)):
    texts_hashes[i] = texts_hashes[i][0]

print(are_texts_similar(texts_hashes[4], texts_hashes[8]))