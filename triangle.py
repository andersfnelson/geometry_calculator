# Name: Anders Nelson
# A Python program to find the area of a triangle.
import math

def prompt():
    print("--------------------------------------------")
    print("PYTHON PROGRAM TO FIND AREA OF A TRIANGLE")
    print("---------------------------------------------")
    first_side = eval(input("Please enter the first side of a triangle: "))
    second_side = eval(input("Please enter the second side of a triangle: "))
    third_side = eval(input("Please enter the third side of a triangle: "))
    print()
    sp = semiperimeter(first_side, second_side, third_side)
    
    print("The perimiter of the triangle is ", perimiter(first_side, second_side, third_side))
    print("The semiperimiter of the triangle is", semiperimeter(first_side, second_side, third_side))
    print("The area of the triangle is ", round(area(first_side, second_side, third_side, sp), 2))
    print("----------------------------------------------")

def perimiter(side1, side2, side3):
    perimiter = side1 + side2 + side3
    return perimiter

def semiperimeter(side1, side2, side3):
    semiperimeter = (side1 + side2 + side3) / 2
    return semiperimeter

def area(side1, side2, side3, semiperimeter):
    area = math.sqrt(semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3))
    return area

if __name__ == '__main__':
    prompt()