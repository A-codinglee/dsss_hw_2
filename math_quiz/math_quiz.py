import random


def Random_Int(min, max):
    """
    Description
    return random integer between given min and max values.
    """
    return random.randint(min, max)


def Random_Op():
    """
    Description
    return one operator among those three.
    """
    return random.choice(['+', '-', '*'])


def Calculator(n1, n2, Op):
    """
    operands : n1, n2
    operator: Op

    using above information, performs calculation.
    """
    prob = f"{n1} {Op} {n2}"
    if Op == '+': ans = n1 + n2
    elif Op == '-': ans = n1 - n2
    else: ans = n1 * n2
    return prob, ans

def math_quiz():
    score = 0
    iter = 10 # total num of quizzes

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    for _ in range(iter):
        # the parameters can be only integer for Random_Int
        n1 = Random_Int(1, 10); n2 = Random_Int(1,6); Op = Random_Op()

        PROBLEM, ANSWER = Calculator(n1, n2, Op)
        print(f"\nQuestion: {PROBLEM}")
        # If the users enter non-valid answer, except statement shows up.
        while True:
            try:
                useranswer = input("Your answer: ")
                useranswer = int(useranswer)
                break  # Exit the loop if input is an integer number.
            except ValueError: # Until the valid input is given, the msg below shows up.
                print("Invalid input! Please enter an integer number.")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{iter}")

if __name__ == "__main__":
    math_quiz()
