def main():
    print("----------------------------------------")
    print("PYTHON PROGRAM TO FIND AREA OF A TRAPEZOID")
    print("----------------------------------------")
    base1 = eval(input("Please enter the base1: "))
    base2 = eval(input("Please enter the base2: "))
    height = eval(input("Please enter the height: "))
    print()
    area = ((base1 + base2)/2) * height
    median = (base1 + base2) / 2
    print("Area of a trapezoid = ", round(area, 2))
    print("Median of a trapezoid = ", round(median, 2))
    print("----------------------------------------")

if __name__ == '__main__':
    main()