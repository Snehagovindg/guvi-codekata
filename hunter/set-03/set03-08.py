in_str = input()

print(''.join(sorted(list(dict.fromkeys(in_str)))))
