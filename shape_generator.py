import math

shape = input("Enter shape (square / rectangle / pyramid / circle / triangle): ").lower()

if shape == "square":
    side = int(input("Enter side of square: "))
    for i in range(side):
        for j in range(side):
            print("*", end=" ")
        print()

elif shape == "rectangle":
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))
    for i in range(breadth):
        for j in range(length):
            print("*", end=" ")
        print()

elif shape == "pyramid":
    height = int(input("Enter height of pyramid: "))
    for i in range(height):
        for j in range(height - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()

elif shape == "circle":
    r = int(input("Enter radius of circle: "))
    for i in range((2 * r) + 1):
        for j in range((2 * r) + 1):
            dist = math.sqrt((i - r) ** 2 + (j - r) ** 2)
            if dist > r - 0.5 and dist < r + 0.5:
                print("*", end="")
            else:
                print(" ", end="")
        print()

elif shape == "triangle":
    height = int(input("Enter height of triangle: "))
    for i in range(1, height + 1):
        for j in range(i):
            print("*", end=" ")
        print()

else:
    print("Invalid Shape!")
