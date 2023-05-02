from collections import OrderedDict


a = str(input().lower())
b = str(input().lower())
b1 = ''.join(OrderedDict.fromkeys(b))
b2 = ''.join(e for e in b1 if e.isalnum())
b3 = ''.join(c for c in b2 if not c.isdigit())


for x in b3:
    print(x, end=' ')
    if x in a:
        for l, count in enumerate(a):
            if count == x:
                print(l + 1, end=' ')
        print()
    else:
        print(None)
