def main():
    # Method to greet the user
    def greeting():
        print("Welcome to the Simple and Compound Interest Calculator!")
        name = input("Please enter your name: ")
        print(f"Hello, {name}!")

    # Method to get user input for principal, time, and rate
    def userinput():
        principal = float(input("Enter the principal amount: $"))
        time = float(input("Enter the number of years: "))
        rate = float(input("Enter the annual interest rate (%): "))
        # Return the collected values to use them in other methods
        return principal, rate, time

    # Method to calculate and display simple interest
    def simpleinterest():
        # Convert the annual interest rate to a decimal
        r = rate / 100
        simplein = (principal * time * r) / 100
        print(f"Simple interest: ${simplein:.2f}")

    # Method to calculate and display compound interest
    def compoundinterest():
        n = float(input("Enter the number of times interest is compounded per year: "))
        r = rate / 100
        amount = principal * (pow((1 + r / n), n * time))
        compound = amount - principal
        print(f"Compound interest: ${compound:.2f}")
        return compound

    # Method to calculate and display the total amount
    def totalamount():
        total = principal + compound
        print(f"Your total is: ${total:.2f}")

    # Method to say goodbye and thank you to the user
    def goodbye():
        print("Thank you for using my interactive program to calculate interests!")
        print("Goodbye!")

    # All methods to run the program
    greeting()
    principal, rate, time = userinput()
    simpleinterest()
    compound = compoundinterest()
    totalamount()
    goodbye()

if __name__ == "__main__":
    main()