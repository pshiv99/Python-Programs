import sys

n = int(input())
phone = dict()

for _ in range(n):
    name, number = input().split()
    phone[name] = number

queries = sys.stdin.readlines()

for name in queries:
    try:
        print('{}={}', name, phone[name])
    except KeyError:
        print('Not found')

