# Project 1 (Quiz Program) - Dayspring Idahosa , Temirlan Stamakunov

import random

def generate_math_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, answer

def generate_science_question():
    questions = [
        "What is the powerhouse of the cell?",
        "What is the chemical symbol for water?",
        "What planet is known as the Red Planet?",
        "What is the largest bone in the human body?",
        "What is the speed of light?",
        "What is the chemical symbol for gold?"
    ]
    random.shuffle(questions)
    return questions[0], "Mitochondria" if "powerhouse" in questions[0] else "H2O" if "water" in questions[0] else "Mars" if "Red Planet" in questions[0] else "femur" if "largest bone" in questions[0] else "299,792 kilometers per second" if "speed of light" in questions[0] else "Au"

def generate_history_question():
    questions = [
        "Who was the first President of the United States?",
        "In which year did World War II end?",
        "What ancient civilization built the pyramids?",
        "Who wrote 'Romeo and Juliet'?",
        "What is the Magna Carta?",
        "What year did the Titanic sink?"
    ]
    random.shuffle(questions)
    return questions[0], "George Washington" if "first President" in questions[0] else "1945" if "World War II end" in questions[0] else "Egyptians" if "pyramids" in questions[0] else "William Shakespeare" if "'Romeo and Juliet'" in questions[0] else "charter of rights" if "Magna Carta" in questions[0] else "1912" if "Titanic sink" in questions[0] else None

def run_quiz(category):
    questions = []
    if category == "Math":
        for _ in range(10):
            questions.append(generate_math_question())
    elif category == "Science":
        for _ in range(10):
            questions.append(generate_science_question())
    elif category == "History":
        for _ in range(10):
            questions.append(generate_history_question())

    correct = 0
    incorrect = 0

    print(f"\nWelcome to the {category} Quiz!\n")

    for i, (question, answer) in enumerate(questions, start=1):
        user_answer = input(f"Question {i}: {question} = ").strip()

        if user_answer.lower() == str(answer).lower():
            print("Correct!\n")
            correct += 1
        else:
            print(f"Incorrect. The correct answer is {answer}.\n")
            incorrect += 1

    print(f"Quiz complete!\nCorrect Answers: {correct}\nIncorrect Answers: {incorrect}")

if __name__ == "__main__":
    print("Choose a quiz category: Math, Science, or History")
    user_category = input().capitalize()

    if user_category in ["Math", "Science", "History"]:
        run_quiz(user_category)
    else:
        print("Invalid category. Please choose Math, Science, or History.")

# Project 2 (Rolling a Dice Game Program) - Dayspring Idahosa , Temirlan Stamakunov

import random

def roll_dice(num_rolls):
    return [random.randint(1, 6) for _ in range(num_rolls)]

def display_rolls(player, rolls):
    print(f"{player}'s rolls: {', '.join(map(str, rolls))}")

def calculate_total_sum(rolls):
    return sum(rolls)

def determine_winner(user_sum, opponent_sum):
    if user_sum > opponent_sum:
        return "You win!"
    elif user_sum < opponent_sum:
        return "Opponent wins!"
    else:
        return "It's a tie!"

def main():
    print("Welcome to the Sophisticated Dice Rolling Game!")

    # Get the number of players
    num_players = int(input("Enter the number of players: "))

    # Get the number of rolls from each player
    num_rolls = int(input("Enter the number of times each player wants to roll the dice: "))

    # Ensure valid inputs
    if num_players <= 0 or num_rolls <= 0:
        print("Please enter a positive number of players and rolls.")
        return

    for player in range(1, num_players + 1):
        print(f"\nPlayer {player}'s turn:")

        # Roll the dice for the current player and the opponent
        user_rolls = roll_dice(num_rolls)
        opponent_rolls = roll_dice(num_rolls)

        # Display rolls for both players
        display_rolls("Your", user_rolls)
        display_rolls("Opponent's", opponent_rolls)

        # Calculate total sums for both players
        user_sum = calculate_total_sum(user_rolls)
        opponent_sum = calculate_total_sum(opponent_rolls)

        # Display total sums and determine the winner
        print(f"\nYour total sum: {user_sum}")
        print(f"Opponent's total sum: {opponent_sum}")

        winner_message = determine_winner(user_sum, opponent_sum)
        print(winner_message)

    print("Thanks for playing!")

if __name__ == "__main__":
    main()