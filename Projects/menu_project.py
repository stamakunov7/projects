# Importing the programs as modules
import assignment_1  # Semester Cost Calculator
import assignment_2  # Home Purchase Tax Calculator
import assignment_3  # Roulette Wheel Simulator
import assignment_3_1  # Interest Calculator
import classassignmentweek_5  # Student Age Analyzer
import assignment_7_1  # Sports Team Management
import assignment_7_2  # Team Statistics Reader
import assignment_8  # Random Number List Generator
import group_assignment  # Quiz and Dice Game

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Semester Cost Calculator: Calculates total semester costs based on credits and course costs.")
        print("2. Home Purchase Tax Calculator: Computes various taxes for a home purchase.")
        print("3. Roulette Wheel Simulator: Simulates a roulette wheel spin.")
        print("4. Interest Calculator: Calculates simple and compound interest.")
        print("5. Student Age Analyzer: Computes current age of students based on birth year.")
        print("6. Sports Team Management: Manages player data for a sports team.")
        print("7. Team Statistics Reader: Reads and displays sports team statistics from a file.")
        print("8. Random Number List Generator: Generates a list of random numbers.")
        print("9. Quiz and Dice Game: Includes a math quiz and a dice roll simulator.")
        print("Enter 'quit' to exit the program.")

        choice = input("Enter your choice: ")

        if choice.lower() == 'quit':
            print("Thank you for using the program. Goodbye!")
            break

        try:
            choice = int(choice)
            if choice == 1:
                assignment_1.main()
            elif choice == 2:
                assignment_2.main()
            elif choice == 3:
                assignment_3.main()
            elif choice == 4:
                assignment_3_1.main()
            elif choice == 5:
                classassignmentweek_5.main()
            elif choice == 6:
                assignment_7_1.main()
            elif choice == 7:
                assignment_7_2.main()
            elif choice == 8:
                assignment_8.main()
            elif choice == 9:
                group_assignment.main()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'quit'.")

if __name__ == "__main__":
    main_menu()
