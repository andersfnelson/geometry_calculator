import cone
import cube
import cuboid
import cylinder
import equilateral_triangle
import sphere
import trapezoid
import triangle

def main():
    while True:
        print("0. Quit")
        print("1. Cone")
        print("2. Cube")
        print("3. Cuboid")
        print("4. Cylinder")
        print("5. Equilateral Triangle")
        print("6. Sphere")
        print("7. Trapezoid")
        print("8. Triangle")
        value = input('Select option: ')
        try:
            value = int(value)
        except:
            pass
        if value == 0:
            break
        elif value == 1:
            cone.prompt()
        elif value == 2:
            cube.prompt()
        elif value == 3:
            cuboid.prompt()
        elif value == 4:
            cylinder.prompt()
        elif value == 5:
            equilateral_triangle.prompt()
        elif value == 6:
            sphere.prompt()
        elif value == 7:
            trapezoid.prompt()
        elif value == 8:
            triangle.prompt()
        else:
            print("Invalid input! Please try again.")
            
if __name__ == '__main__':
    main()