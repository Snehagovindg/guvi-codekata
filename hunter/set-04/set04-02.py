def even_positions(indict):
    nn = len(indict)
    results = {}
    for i, k, v in zip(range(nn), indict.keys(), indict.values()):
        if (i+1) % 2 == 0:
            results[k] = v

    if len(results) == 1:
        print(list(results.keys())[0])
    else:
        even_positions(results)


n = int(input())
in_list = list(map(int, input().split()))

in_dict = {i: in_list[i] for i in range(n)}

even_positions(in_dict)
