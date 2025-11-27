class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)

l1 = int(input("Enter length of first rectangle:"))
b1 = int(input("Enter breadth of first rectangle:"))
r1 = Rectangle(l1,b1)
print("Rectangle 1: Area =", r1.area(), "Perimeter =", r1.perimeter())

l2 = int(input("Enter length of first rectangle:"))
b2 = int(input("Enter breadth of first rectangle:"))
r2 = Rectangle(l2,b2)
print("Rectangle 2: Area =", r2.area(), "Perimeter =", r2.perimeter())

if r1.area() > r2.area():
    print("Rectangle 1 has a larger area")
elif r1.area() < r2.area():
    print("Rectangle 2 has a larger area")
else:
    print("Both rectangles have the same area")