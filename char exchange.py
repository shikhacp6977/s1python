s = input("Enter a string: ")

if len(s) > 1:
    new_str = s[-1] + s[1:-1] + s[0]
else:
    new_str = s
print(new_str)