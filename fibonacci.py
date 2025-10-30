num=int(input("enter number:"))
a=0
b=1
print("Fibonacci series:")
for i in range(num):
    print(a , end=" ")
    a , b = b , a + b