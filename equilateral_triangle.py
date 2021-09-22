def main():
    import math
    print("------------------------------------------")
    print("PYTHON PROGRAM TO FIND AREA OF AN EQUILATERAL TRIANGLE")
    print("------------------------------------------")
    print()
    side_length = eval(input("Please enter length of any side of an equilateral triangle: "))
    area =((math.sqrt(3)) / 4) * side_length**2
    perimeter = 3 * side_length
    semiperimeter = (3 * side_length) / 2
    altitude = (side_length / 2) * math.sqrt(3)
    print("Area of equilateral triangle = ", round(area, 2))
    print("Perimeter of equilateral triangle = ", round(perimeter, 2))
    print("Semi Perimeter of equilateral triangle = ", round(semiperimeter, 2))
    print("Altitude of equilateral triangle = ", round(altitude, 2))

if __name__ == '__main__':
    main()