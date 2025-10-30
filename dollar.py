string= input("Enter the string:")
first_char=string[0]
new_string=first_char
l=len(string)
for i in range(1,l):
   if string[i] == first_char:
       new_string += "$"
   else:
       new_string += string[i]
print(new_string)