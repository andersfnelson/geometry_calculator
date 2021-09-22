def main():
    print("PYTHON PROGRAM TO FIND VOLUME AND SURFACE AREA OF A CUBOID")
    print("----------------------------------------------------------")
    length = eval(input("Please enter the length: "))
    width = eval(input("Please enter the width: "))
    height = eval(input("Please enter the height: "))
    print()
    surface_area = (2 * (length * width)) + (2 * (length * height)) + (2 * (height * width))
    volume = (length * width * height)
    lateral_surface_area = (2 * (height * length)) + (2 * (height * width))
    print("The surface area of a cuboid = ", round(surface_area, 2))
    print("The volune of a cuboid = ", round(volume, 2))
    print("The lateral surface area of a cuboid = ", round(lateral_surface_area, 2))

if __name__ == '__main__':
    main()
