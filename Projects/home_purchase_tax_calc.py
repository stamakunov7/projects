def main():

    # all taxes
    statetax = 0.05
    countytax = 0.025
    realtortax = 0.05

    # Welcoming to the program
    name = input("Hello, welcome to my program! What is your name? : ")
    print("Welcome,", name)

    # input from the user: purchase price of the home
    purchase_price = float(input("Enter the purchase price of the home: $"))
    print(f"Amount of purchase: ${purchase_price: .3f}")

    # Mathematical calculations and formulas, calculating the taxes, totals
    statesalestax = purchase_price * statetax
    print(f"State sales tax: ${statesalestax: .3f}")
    countysalestax = purchase_price * countytax
    print(f"County sales tax: ${countysalestax: .3f}")
    totalsalestax = countysalestax + statesalestax
    print(f"Total sales tax: ${totalsalestax: .3f}")
    totalpurchaseamount = purchase_price + totalsalestax
    print(f"Total sale amount: ${totalpurchaseamount: .3f}")
    realtor = purchase_price * realtortax
    print(f"Realtor commission: ${realtor: .3f}")

if __name__ == "__main__":
    main()
# Reflection and challanges:
# I didn't face any challanges with this assignment, I did it in 15 minutes :)