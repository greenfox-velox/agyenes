# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

def print_triangle(lines):
    i = 0
    while i <= lines:
        print(i * '*')
        i += 1

print_triangle(8)
