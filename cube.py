# Name: Anders Nelson
# A program to find the volume and surface area of a cube.

def main():
    print("---------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME AND SURFACE AREA OF A CUBE")
    print("----------------------------------------------")
    side_length = eval(input("Please enter the length of any side of a cube: "))
    print()
    surface_area = 6 * side_length**2
    volume = side_length**3
    lateral_surface_area = 4 * side_length**2
    print("Surface area of a cube = ", round(surface_area, 2))
    print("Volume of cube = ", round(volume, 2))
    print("Lateral surface area of cube = ", round(lateral_surface_area, 2))

if __name__ == '__main__':
    main()