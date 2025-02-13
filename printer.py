def print_sunset():
    width = 21

    # Print the sun (semi-circle shape)
    for i in range(3):
        for j in range(width):
            if width // 2 - i * 3 <= j <= width // 2 + i * 3:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Sun rays
    for i in range(2):
        for j in range(width):
            if j % 4 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Horizon line
    print("*" * width)

    # Water reflection
    for i in range(3):
        for j in range(width):
            if width // 2 - i * 2 <= j <= width // 2 + i * 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Waves
    for i in range(2):
        for j in range(width):
            if j % 2 == 0:
                print("~", end="")
            else:
                print(" ", end="")
        print()


print_sunset()
