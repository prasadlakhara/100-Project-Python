def print_square_pattern(n):
    """Print a square pattern of stars."""
    for i in range(n):
        print("* " * n)

def print_triangle_pattern(n):
    """Print a right-angle triangle pattern of stars."""
    for i in range(1, n + 1):
        print("* " * i)

def print_pyramid_pattern(n):
    """Print a pyramid pattern of stars."""
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

def print_number_pyramid(n):
    """Print a number pyramid pattern."""
    for i in range(1, n + 1):
        print(" " * (n - i) + " ".join(str(x) for x in range(1, i + 1)))

def print_inverted_triangle(n):
    """Print an inverted triangle pattern."""
    for i in range(n, 0, -1):
        print("* " * i)

def print_floyds_triangle(n):
    """Print Floyd's triangle (number pattern)."""
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

def main():
    print("Welcome to the Pattern Generator!")
    print("Select the pattern type:")
    print("1. Square Pattern")
    print("2. Right-Angle Triangle Pattern")
    print("3. Pyramid Pattern")
    print("4. Number Pyramid")
    print("5. Inverted Triangle Pattern")
    print("6. Floyd's Triangle")

    choice = input("Enter the pattern type number (1-6): ")

    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice, please choose a valid option (1-6).")
        return

    n = int(input("Enter the size of the pattern: "))

    if choice == '1':
        print_square_pattern(n)
    elif choice == '2':
        print_triangle_pattern(n)
    elif choice == '3':
        print_pyramid_pattern(n)
    elif choice == '4':
        print_number_pyramid(n)
    elif choice == '5':
        print_inverted_triangle(n)
    elif choice == '6':
        print_floyds_triangle(n)

if __name__ == "__main__":
    main()
