#Creation of documentation (help)
def add(x, y):
    """Returns the sum of x and y."""
    return x + y

help(add)

def getLengthOfEndingParts(input):
    x = input.split("@")[1]
    x = x.split(".")
    return len(x)

def sortByLength(listToSort):
    return sorted(listToSort, key=lambda w: getLengthOfEndingParts(w))

testList = ["abc.xyz@serwer.o.bardzo.dlugiej.nazwie.com", "jan.kot@gmail.com", "dsan@kis.p.lodz.pl"]
sortedList = sortByLength(testList)
print(testList)
print(sortedList)