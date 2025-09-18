numbers=[-5,9,-2,3,6]
positivenumbers = [num for num in numbers if num > 0]
print(positivenumbers)


n=5
square=[x**2 for x in range(1,n+1)]
print(square)


word="Shikha"
vowels=[ch for ch in word if ch in "aeiou"]
print(vowels)


word = "SFGJ"
ordinals=[ord(ch) for ch in word ]
print(ordinals)