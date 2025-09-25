num=input("Enter a list of integers:")
numbers= num.split()
result = []
for num in numbers:
    num = int(num)
    if num > 100:
        result.append('over')
    else:
        result.append(num)
print(result)