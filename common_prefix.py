from itertools import takewhile

s = 'kot'
sa = 'kotek'

ini_strlist = [s, sa]

res = ''.join(c[0] for c in takewhile(lambda x: all(x[0] == y for y in x), zip(*ini_strlist)))

print(str(res))
