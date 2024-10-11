import random

def generate_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*', '/'])
    
    if operation == '+':
        results = num1 + num2
    elif operation == '-':
        results = num1 - num2
    elif operation == '*':
        results = num1 * num2
    elif operation=='/':
        results = num1/num2

    
    return f"{num1} {operation} {num2}", results

def play_game():
    score = 0
    num_problems = 5

    print("Welcome to our Python Calculator Game!")
    print(f"Solve {num_problems} problems.\n")

    for i in range(1, num_problems + 1):
        problem, results = generate_problem()
        print(f"Problem {i}: {problem}")
        
        
        while True:
            try:
                player_answer = float(input("Your answer: "))
                break
            except ValueError:
                print("Invalid input, please enter the correct number")
        
        # Check if the anser provided by the player is correct
        if player_answer == results:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {results}.\n")

    # Grading the player
    print(f"Game Over! Your final score is {score}/{num_problems}.")

# Start the game
if __name__ == "__main__":
    play_game()
