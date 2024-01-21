def main():
    # Prompt the user to input their name
    welcome = input("Input your name please: ")

    # Display a welcome message with the user's name
    print("Welcome to my program,", welcome)

    # Prompt the user to input a pocket number
    value = int(input("Spin the wheel - valid pocket number is from 0 to 36: "))

    # Check if the entered value is outside the valid range
    if 0 >= value >= 36:
        # Display an error message for an invalid value
        print("Not a valid value!")

    else:
        # Check the color of the pocket based on the specified rules
        if value >= 1 and value <= 10:
            if value % 2:
                print("Your pocket is - Red")
            else:
                print("Your pocket is - Black")

        elif value >= 11 and value <= 18:
            if value % 2:
                print("Your pocket is - Black")
            else:
                print("Your pocket is - Red")

        elif value >= 19 and value <= 28:
            if value % 2:
                print("Your pocket is - Red")
            else:
                print("Your pocket is - Black")

        elif value >= 29 and value <= 36:
            if value % 2:
                print("Your pocket is - Black")
            else:
                print("Your pocket is - Red")

        elif value == 0:
            print("Your pocket is - Green")

if __name__ == "__main__":
    main()