"""
https://stepik.org/lesson/41234/step/2
"""
import sys
sys.setrecursionlimit(2000)

n = int(next(sys.stdin))
parents_list = [int(parent) for parent in next(sys.stdin).split()]
parents_dict = dict(enumerate(parents_list))
parents_list = [0 for i in range(n)]


def from_child_to_root(child, level):
    if parents_list[child] or parents_dict[child] == -1:
        return parents_list[child] + level - 1
    else:
        return from_child_to_root(parents_dict[child], level + 1) 

depth = 1
for child in parents_dict:
    curr_depth = from_child_to_root(child, 1)
    parents_list[child] = curr_depth
    if curr_depth > depth:
        depth = curr_depth

print(depth + 1)

