# Name: Anders Nelson
# # A Python program to find the volume and surface area of a cylinder.

def main():
    import math
    print("------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A CYLINDER")
    print("------------------------------------------------------")
    radius = eval(input("Please enter the radius: "))
    height = eval(input("Please enter the height: "))
    print()
    surface_area = (2 * math.pi * radius * height) + (2 * math.pi * radius**2)
    volume = math.pi * (radius**2) * height
    lateral_surface_area = 2 * math.pi * radius * height
    top_bottom_surface_area = math.pi * (radius**2)
    print("The surface area of a Cylinder = ", round(surface_area, 2))
    print("The volume of a Cylinder = ", round(volume, 2))
    print("Lateral surface area of a Cylinder = ", round(lateral_surface_area, 2))
    print("Top OR bottom surface area of a Cylinder = ", round(top_bottom_surface_area, 2))
    print("-------------------------------------------------------")
if __name__ == '__main__':
    main()