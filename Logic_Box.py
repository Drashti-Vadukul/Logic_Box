print("Welcome to the Pattern Generator and Number Analyzer!")

while True:

    print()
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    num = int(input("Enter your choice: "))

    # Option 1 - Pattern
    if num == 1:

        rows = int(input("Enter the number of rows for the pattern: "))

        print()
        print("Pattern:")

        for i in range(1, rows + 1):
            print("*" * i)

    # Option 2 - Number Analyzer
    elif num == 2:

        print()
        first = int(input("Enter the First of the range: "))
        last = int(input("Enter the Last of the range: "))

        total = 0

        for i in range(first, last + 1):

            if i % 2 == 0:
                print("Number", i, "is Even")
            else:
                print("Number", i, "is Odd")

            total = total + i

        print("Sum of all numbers from", first, "to", last, "is:", total)

    # Option 3 - Exit
    elif num == 3:

        print("Exiting the program. Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please select 1, 2, or 3.")