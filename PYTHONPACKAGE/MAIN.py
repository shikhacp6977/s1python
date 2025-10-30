from TWO_D.circle import area as cirarea,perimeter as cirperimeter
from TWO_D.rectangle import area as rectarea,perimeter as rectperimeter
from TWO_D.THREE_D.sphere import area as spherearea,perimeter as sphereperimeter
from TWO_D.THREE_D.cuboid import area as cuboidarea,perimeter as cuboidperimeter

print("circle area:",cirarea(4))
print("circle perimeter:",cirperimeter(4))

print("rectangle area:",rectarea(5,6))
print("rectangle perimeter:",rectperimeter(5,6))

print("sphere area:",spherearea(3))
print("sphere perimeter:",sphereperimeter(3))

print("cuboid area:",cuboidarea(3,6,4))
print("cuboid perimeter:",cuboidperimeter(3,6,4))