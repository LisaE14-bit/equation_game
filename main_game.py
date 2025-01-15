import random

def generate_equation():
    """
    Generates a random equation of the form: a × x = b.
    Returns the equation as a string and the correct value of x.
    """
    a = random.randint(1, 10)
    x = random.randint(1, 10)
    b = a * x
    equation = f"{a} × x = {b}"
    return equation, x

def check_answer(user_answer, correct_answer):
    """
    Validates the user's answer and returns True if correct, False otherwise.
    """
    return user_answer == correct_answer

def display_score(score, total_questions):
    """
    Displays the user's total score at the end of the game.
    """
    print(f"GAME OVER! Your total score is {score}/{total_questions}.")

def main():
    """
    Main function to run the game.
    """
    print("Welcome to the Equation Game!")
    total_questions = 3
    score = 0

    for i in range(total_questions):
        equation, correct_answer = generate_equation()
        print(f"Question {i + 1}: {equation}")

        try:
            user_answer = int(input("Your answer for x: "))
            if check_answer(user_answer, correct_answer):
                print("That's Right!")
                score += 1
            else:
                print(f"This is incorrect! The correct answer was {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    display_score(score, total_questions)

if __name__ == "__main__":
    main()
