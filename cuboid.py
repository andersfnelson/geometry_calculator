def prompt():
    print("PYTHON PROGRAM TO FIND VOLUME AND SURFACE AREA OF A CUBOID")
    print("----------------------------------------------------------")
    length = eval(input("Please enter the length: "))
    width = eval(input("Please enter the width: "))
    height = eval(input("Please enter the height: "))
    print()
    print("The surface area of a cuboid = ", round(surface_area(length, width, height), 2))
    print("The volune of a cuboid = ", round(volume(length, width, height), 2))
    print("The lateral surface area of a cuboid = ", round(lateral_surface_area(length, width, height), 2))

def surface_area(length, width, height):
    surface_area = (2 * (length * width)) + (2 * (length * height)) + (2 * (height * width))
    return surface_area

def volume(length, width, height):
    volume = (length * width * height)
    return volume

def lateral_surface_area(length, width, height):
    lateral_surface_area = (2 * (height * length)) + (2 * (height * width))
    return lateral_surface_area

if __name__ == '__main__':
    prompt()
