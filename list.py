list1=[1,2,3,4,5]
list2=[2,4,6,8]
print("Elements in list1 is:",list1)
print("Elements in list2 is:",list2)
if len(list1) == len(list2):
    print("Lists have same length")
else:
    print("Lists have different length")
s1=0
s2=0
for i in range(len(list1)):
    s1=s1+list1[i]
print("The sum of list1 is:",s1)
for i in range(len(list2)):
    s2=s2+list2[i]
print("The sum of list1 is:",s2)
if s1==s2:
    print("The sum of list1 and list2 are same")
else:
    print("The sum of list1 and list2 are different")
print("The common elements in lists is:")
for i in list1:
    for j in list2:
        if i==j:
            print(i)