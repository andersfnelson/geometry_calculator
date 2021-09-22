# Name: Anders Nelson
# A Python program to find the area of a triangle.

def main():
    import math
    print("--------------------------------------------")
    print("PYTHON PROGRAM TO FIND AREA OF A TRIANGLE")
    print("---------------------------------------------")
    first_side = eval(input("Please enter the first side of a triangle: "))
    second_side = eval(input("Please enter the second side of a triangle: "))
    third_side = eval(input("Please enter the third side of a triangle: "))
    print()
    perimiter = first_side + second_side + third_side
    semiperimiter = (1/2) * perimiter
    area = math.sqrt(semiperimiter * (semiperimiter - first_side) * (semiperimiter - second_side) * (semiperimiter - third_side))
    print("The perimiter of the triangle is ", perimiter)
    print("The semiperimiter of the triangle is", semiperimiter)
    print("The area of the triangle is ", round(area, 2))
    print("----------------------------------------------")

if __name__ == '__main__':
    main()