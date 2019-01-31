from itertools import permutations

in_str = input()

out_list = permutations(in_str)
out_list = list(dict.fromkeys(out_list))

for perm in out_list:
    print(''.join(perm))
