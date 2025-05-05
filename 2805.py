import math
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
wood_list = list(map(int, input().split()))
wood_list.append(0)

wood_dic = dict()

for wood in wood_list:
    if wood in wood_dic:
        wood_dic[wood] += 1
    else:
        wood_dic[wood] = 1

sorted_key = sorted(wood_dic.keys(), reverse=True)

height = sorted_key[0]
cur_count = 0
cur_idx = -1
sum = 0

while sum < m:
    cur_idx += 1
    height = sorted_key[cur_idx]
    cur_count += wood_dic[height]
    remain_height = height - sorted_key[cur_idx + 1]

    if sum + cur_count * remain_height >= m:
        d = math.ceil((m - sum) / cur_count)
        print(height - d) # height + d 틀림
        break
    else:
        sum += cur_count * remain_height