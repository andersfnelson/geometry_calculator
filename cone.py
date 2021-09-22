# Name: Anders Nelson
# # A Python program to find the volume and surface area of a cone.

def main():
    import math
    print("------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A CONE")
    print("------------------------------------------------------")
    radius = eval(input("Please enter the radius: "))
    height = eval(input("Please enter the height: "))
    print()
    slant = math.sqrt(height**2 + radius**2)
    surface_area = math.pi * radius * (radius + (math.sqrt(height**2 + radius**2)))
    volume = math.pi * (radius**2) * (height/3)
    lateral_surface_area = radius * math.pi * (math.sqrt(height**2 + radius**2))
    print("Length of a Side (Slant) of a Cone = ", round(slant, 2))
    print("The surface area of a Cone = ", round(surface_area, 2))
    print("The volume of a Cone = ", round(volume, 2))
    print("Lateral surface area of a Cone = ", round(lateral_surface_area, 2))
    print("-------------------------------------------------------")

if __name__ == '__main__':
    main()