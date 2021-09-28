import math

def prompt():
    print("------------------------------------------")
    print("PYTHON PROGRAM TO FIND AREA OF AN EQUILATERAL TRIANGLE")
    print("------------------------------------------")
    print()
    side_length = eval(input("Please enter length of any side of an equilateral triangle: "))
    print("Area of equilateral triangle = ", round(area(side_length), 2))
    print("Perimeter of equilateral triangle = ", round(perimeter(side_length), 2))
    print("Semi Perimeter of equilateral triangle = ", round(semiperimeter(side_length), 2))
    print("Altitude of equilateral triangle = ", round(altitude(side_length), 2))

def area(side_length):
    area =((math.sqrt(3)) / 4) * side_length**2
    return area

def perimeter(side_length):
    perimeter = 3 * side_length
    return perimeter

def semiperimeter(side_length):
    semiperimeter = (3 * side_length) / 2
    return semiperimeter

def altitude(side_length):
    altitude = (side_length / 2) * math.sqrt(3)
    return altitude


if __name__ == '__main__':
    prompt()