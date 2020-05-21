from collections import Counter

strd = 'geekforgeeks'

print('the original string is:\n',strd)

res = [ i for i, count in Counter(strd).items() if count & 1  ]

print ("odd frequency of string is:\n", res )
