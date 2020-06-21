import collections
import sys

words = sys.stdin.read().strip().split()

count = collections.defaultdict(int)

for i in words:
    index = 0
    for j in i:
        index = index + ord(j)
    print(index)

    count[index] = count[index] + 1

l = [item for item in count.values()]

print(sorted(l))