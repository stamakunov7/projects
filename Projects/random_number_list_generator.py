import random

# Function to generate a list of seven random numbers
def numbers():
    first = []

    # Generate seven random numbers in the range of 0-9
    for i in range(1, 8):
        a = random.randint(0, 9)
        first.append(a)

    return first

# Main function to run the program
def main():
    # Continuous loop to allow the user to run the program again
    while True:
        # Generate a list of seven random numbers
        first = numbers()

        # Display the list, total, maximum, and minimum values of the numbers
        print(f"List of numbers: {first}")
        print("Total of all numbers:", sum(first))
        print("Maximum Value:", max(first))
        print("Minimum Value:", min(first))

        # Calculate and display the average value rounded to two decimal places
        average = round(sum(first) / len(first), 2)
        print(f"Average: {average}")

        # Convert the list to a tuple and display it
        tuplefirst = tuple(first)
        print(f"The list converted to tuple has the following values: {tuplefirst}")

        # Ask the user if they want to run the program again
        user_input = input("Do you want to run the program again? (y/n): ")
        if user_input != "y":
            # Break out of the loop if the user enters anything other than 'y'
            break

        print()

    # Display a thank you message when the user decides not to run the program again
    print("Thank you for using my program!")

# Check if the script is being run directly
if __name__ == '__main__':
    main()