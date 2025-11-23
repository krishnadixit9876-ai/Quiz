# **Quiz Application**

def run_quiz():
    print("Welcome to the Quiz!")
    print("Answer the following questions by typing the correct option (a, b, c, or d).")
    print("-" * 50)

    # Quiz questions and answers
    questions = {
        "What is the capital of India?": {
            "options": ["a) Mumbai", "b) Delhi", "c) Kolkata", "d) Chennai"],
            "answer": "b"
        },
        "Which programming language is known as the backbone of web development?": {
            "options": ["a) Python", "b) Java", "c) JavaScript", "d) C++"],
            "answer": "c"
        },
        "What is the square root of 64?": {
            "options": ["a) 6", "b) 7", "c) 8", "d) 9"],
            "answer": "c"
        },
        "Who wrote the book '1984'?": {
            "options": ["a) George Orwell", "b) J.K. Rowling", "c) Ernest Hemingway", "d) Mark Twain"],
            "answer": "a"
        }
    }

    score = 0

    # Loop through questions
    for question, details in questions.items():
        print("\n" + question)
        for option in details["options"]:
            print(option)
        
        # Get user input
        user_answer = input("Your answer: ").lower()
        
        # Check if the answer is correct
        if user_answer == details["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {details['answer']}.")

    # Display final score
    print("\n" + "-" * 50)
    print(f"Quiz Over! Your final score is {score}/{len(questions)}.")
    if score == len(questions):
        print("Excellent! You got all the answers right!")
    elif score > len(questions) // 2:
        print("Good job! You did well.")
    else:
        print("Better luck next time!")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
