def prompt():
    print("----------------------------------------")
    print("PYTHON PROGRAM TO FIND AREA OF A TRAPEZOID")
    print("----------------------------------------")
    base1 = eval(input("Please enter the base1: "))
    base2 = eval(input("Please enter the base2: "))
    height = eval(input("Please enter the height: "))
    print()
    print("Area of a trapezoid = ", round(area(base1, base2, height), 2))
    print("Median of a trapezoid = ", round(median(base1, base2), 2))
    print("----------------------------------------")

def area(base1, base2, height):
    area = ((base1 + base2)/2) * height
    return area

def median(base1, base2):
    median = (base1 + base2) / 2
    return median

if __name__ == '__main__':
    prompt()