__author__ = 'Bradley'

from collections import Counter, defaultdict, OrderedDict

items = ['F', 'C', 'C', 'A', 'B', 'A', 'C', 'E', 'F']

cntr = Counter(items)
print(cntr)
cntr['C'] -= 1
print(cntr)

d = defaultdict(int)

for item in items:
    d[item] += 1

print(d)

nums = range(10)

odd_squares = [x * x for x in nums if x % 2]
sum(odd_squares)

print(sum(odd_squares))

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

odds = filter(lambda x: x % 2, nums)
odd_squares = map(lambda x: x * x, odds)
sum = reduce(lambda x, y: x + y, odd_squares)

print(sum)