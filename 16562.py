import math
import sys

input = sys.stdin.readline

def find(union, idx):
    if union[idx] != idx:
        union[idx] = find(union, union[idx])
        return union[idx]
    else:
        return idx

def union(union, money_list, a, b):
    a_parent = find(union, a)
    b_parent = find(union, b)

    if a_parent == b_parent:
        return

    a_money = money_list[a_parent]
    b_money = money_list[b_parent]

    if b_money >= a_money:
        union[b_parent] = a
    else:
        union[a_parent] = b


n, m, k = map(int, input().split())
money_list = list(map(int, input().split()))
friend_graph = { i : [i] for i in range(n)}
union_graph = [ i for i in range(n)]

for _ in range(m):
    v, u = map(int, input().split())
    v -= 1
    u -= 1

    union(union_graph, money_list, v, u)

visited = [False for _ in range(n)]

sum = 0

for i in range(n):
    parent = find(union_graph, i)

    if not visited[parent]:
        sum += money_list[parent]
        visited[parent] = True

if sum <= k:
    print(sum)
else:
    print("Oh no")