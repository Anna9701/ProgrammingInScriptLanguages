# grupa A

def one_sentence_with_stars(param):
    return param.replace(" ", "*")

assert one_sentence_with_stars("Glupie_zdanie") == "Glupie_zdanie"
assert one_sentence_with_stars("A  normal sentence.") == "A**normal*sentence."

def two_sentence_with_stars2(s):
    return "*".join(s.split())

assert two_sentence_with_stars2("Glupie_zdanie") == "Glupie_zdanie"
assert two_sentence_with_stars2("A  normal sentence.") == "A*normal*sentence."

def three_sum_middle_column(s):
    return s.split

# test = """50 abc 1.5 5
# -12 def 2.75 1
# 35 gh 3 2
# 1000 ijkl -4.35 33"""


def four_count_unique_digits(n):
    return len(set(str(n)))

assert four_count_unique_digits(245) == 3
assert four_count_unique_digits(222) == 1
assert four_count_unique_digits(244) == 2

def five_divisors(n):
    return len([x for x in range(1, n) if n/x==int(n/x)])

assert five_divisors(4) == 2
assert five_divisors(12) == 5
assert five_divisors(8) == 3

def six_intersections(*sets):
    return 0

#assert six_intersections(set([1, 2, 3]), set([3, 5]), set([2, 1, 10]), set([4, 10])) == [{3}, {1, 2}, set()]
#assert six_intersections(set([1, 2, 3])) == []

def seven_easy(li):
    return [x for x in reversed(li) if x % 3 == 0 and x % 5 != 0]

assert seven_easy([2, 3, 4, 5, 6]) == [6, 3]
assert seven_easy([5, 15, 21, 25, 30, 33]) == [33, 21]
assert seven_easy([7, 12, 13, 15, 19, 300, 39]) == [39, 12]

def eight_diagonal1():
    return [''.join(x) for x in list(map(list,zip([str(chr(i)) for i in range(ord('a'),ord('h')+1)],[str(x) for x in range(8, 0, -1)])))]
assert eight_diagonal1() == ["a8", "b7", "c6", "d5", "e4", "f3", "g2", "h1"]

def nine_diagonal2():
    return list(map(tuple,zip([str(chr(i)) for i in range(ord('a'),ord('h')+1)],[x for x in range(1, 9)])))

assert nine_diagonal2() == [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5), ("f", 6), ("g", 7), ("h", 8)]

#def ten_silly_poem(s):
# assert ten_silly_poem("There live a green giant whose name was
# Sam. His hair was the color of strawberry jam.") == """ There
#  live
#  a
#  green
#  giant
#  whose
#  name
#  was
#  Sam.
#  His
#  hair
#  was
#  the
#  color
#  of
# strawberry
#  jam. """

def eleven_even(set_):
    return all(elem % 2 == 0 for elem in set_)

assert eleven_even([2, 4, 6, 8, 10]) == True
assert eleven_even([2, 4, 5, 13, 76, 99, 6, 8, 10]) == False