import string


code = str(input())
decode = str(input())
abc = string.ascii_lowercase
decode_abc = dict(zip(list(decode), list(abc)))

for i in code:
    if i in decode_abc:
        print(decode_abc.get(i), end='')
    else:
        print(i, end='')
