# Name: Anders Nelson
# A program to find the volume and surface area of a cube.

def prompt():
    print("---------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME AND SURFACE AREA OF A CUBE")
    print("----------------------------------------------")
    side_length = eval(input("Please enter the length of any side of a cube: "))
    print()
    print("Surface area of a cube = ", round(surface_area(side_length), 2))
    print("Volume of cube = ", round(volume(side_length), 2))
    print("Lateral surface area of cube = ", round(lateral_surface_area(side_length), 2))

def surface_area(side_length):
    surface_area = 6 * side_length**2
    return surface_area

def volume(side_length):
    volume = side_length**3
    return volume

def lateral_surface_area(side_length):
    lateral_surface_area = 4 * side_length**2
    return lateral_surface_area

if __name__ == '__main__':
    prompt()