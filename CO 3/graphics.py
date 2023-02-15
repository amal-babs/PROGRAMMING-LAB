from graphics.rectangle import*
from graphics.circle import*
from graphics.ThreeDgraphics.cuboid import*
from graphics.ThreeDgraphics.sphere import*

l=int(input("enter the length of rectangle:"))
b=int(input("enter the breadth of rectangle:"))
print("area of rectangle:",RectArea(l,b))
print("perimeter of rectangle:",RectPerimeter(l,b))

r=int(input("enter the radius of circle:"))
print("area of circle:",CirArea(r))
print("perimeter of circle:", CirPrimeter(r))

l=int(input("enter the length of cuboid:"))
b=int(input("enter the breadth of cuboid:"))
h=int(input("enter the height of cuboid:"))
print("area of cubiod:",Area(l,b,h))
print("perimeter of cuboid:",PeRimeter(l,b,h))

r=int(input("enter the radius of sphere:"))
print("area of sphere:",spArea(r))
print("perimeter of sphere:", spperi(r))

