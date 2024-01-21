def main():
    # Initialize a variable to keep track of the total ages and current year
    ages = 0
    year = 2023

    # Use a loop to get the age of each of the 4 students
    for a in range(4):
        # Prompt the user to enter the age of the current student
        birthyear = int(input(f"Enter the birth year of student {a + 1}: "))

        # Calculating a students age by subtracting their birthyear from current
        age = year - birthyear
        print(f"Student {a+1} age is: {age}")
        # Add the student's age to the total ages
        ages += age

    # Calculate the average age for all the students
    average_age = ages / 4

    # Print the average age rounded to the nearest integer
    print("The average age for the students is:", round(average_age))

    # Define a function called 'letsgo' to make a method
    def letsgo():
        # Use a loop to iterate through 4 students
        for student in range(4):
            # Initialize a variable to store the total score for the current student
            total_score = 0

            # Use another loop to get the exam scores for each student (3 exams)
            for exam in range(3):
                # Asking the user to input the exam score for the current student and exam
                score = float(input(f"Enter the score for student {student+1}, exam {exam+1}: "))

                # Add the current exam score to the total score for this student
                total_score += score

            # Calculate the average score for each student
            average_score = total_score / 3

            # Determine the letter grade based on the average score
            if average_score >= 90:
                grade = "A"
            elif average_score >= 80:
                grade = "B"
            elif average_score >= 70:
                grade = "C"
            elif average_score >= 60:
                grade = "D"
            else:
                grade = "F"

            # Print the results for the each student, including average score and letter grade
            print(f"For student {student+1}, the average score is {average_score}, the letter grade is {grade}")

    # Call the 'letsgo' function to run the program
    letsgo()

if __name__ == "__main__":
    main()