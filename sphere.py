#Name: Anders Nelson
#A program that outputs the volume and surface area of a sphere.

def main():
    import math
    print("-------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME AND SURFACE AREA OF SPHERE")
    print("-------------------------------------------------")
    radius = eval(input("Please enter the radius: "))
    surface_area = 4 * math.pi * radius**2
    volume = (4/3) * math.pi * radius**3
    print("The surface area of the sphere = ", round(surface_area, 2))
    print("The volume of the sphere = ", round(volume, 2))
    print("--------------------------------------------------")

if __name__ == '__main__':
    main()