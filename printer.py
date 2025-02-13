def print_filled_sunset():
    width = 21
    height = 10
    sun_center = width // 2
    sun_radius = 4

    for i in range(height):
        for j in range(width):
            # Draw the sun as a filled circle
            if (i - 4) ** 2 + (j - sun_center) ** 2 <= sun_radius ** 2:
                print("*", end="")
            # Draw the horizon line
            elif i == 5:
                print("=", end="")
            # Draw water with a wavy pattern
            elif i > 5:
                print("*", end="")
            # Sky above the sun
            else:
                print("*", end="")
        print()

print_filled_sunset()
