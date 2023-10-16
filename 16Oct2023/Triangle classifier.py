side1=float(input("Enter side 1 of the triangle:\n"))
side2=float(input("Enter side 2 of the triangle:\n"))
side3=float(input("Enter side 3 of the triangle:\n"))

if side1==side2==side3:
    print("The triangle is equilateral triangle")
elif side1!=side2 and side2!=side3 and side1!=side3:
    print("the triagle is Scalene  triangle")
else:
    print("the triangle is isosceles triangle")



