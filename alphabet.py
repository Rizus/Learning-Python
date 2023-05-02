import string


text = str(input().lower())

alphabet = "".join(x for x in text if x in string.ascii_letters)
print("".join(sorted(list(set(alphabet)))))
