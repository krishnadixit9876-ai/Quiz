# Quiz Application

A simple, interactive command-line quiz application built with Python that tests your knowledge across various topics including geography, programming, mathematics, and literature.

## Description

This Quiz Application is a beginner-friendly Python program that presents users with multiple-choice questions and provides instant feedback on their answers. The application features a clean interface, score tracking, and personalized feedback based on performance.

## Features

- **Interactive Command-Line Interface**: Easy-to-use text-based interface
- **Multiple-Choice Questions**: Four questions covering diverse topics
- **Instant Feedback**: Get immediate responses on whether your answer is correct
- **Score Tracking**: Automatic calculation of your final score
- **Performance-Based Messages**: Receive personalized feedback based on your results
- **Simple Input System**: Answer questions by typing a single letter (a, b, c, or d)

## Requirements

- Python 3.x (Python 3.6 or higher recommended)
- No external libraries required - uses only Python standard library

## Installation

1. Clone or download this repository to your local machine
2. Ensure Python 3.x is installed on your system
3. Navigate to the directory containing `quiz.py`

## Usage

Run the quiz application using Python:

```bash
python quiz.py
```

### How to Play

1. The application will welcome you and display the first question
2. Read each question carefully along with the four options (a, b, c, d)
3. Type your answer as a single letter (case-insensitive)
4. Press Enter to submit your answer
5. Receive instant feedback on whether you're correct
6. Continue through all questions
7. View your final score and performance feedback

### Example Session

```
Welcome to the Quiz!
Answer the following questions by typing the correct option (a, b, c, or d).
--------------------------------------------------

What is the capital of India?
a) Mumbai
b) Delhi
c) Kolkata
d) Chennai
Your answer: b
Correct!
```

## Quiz Questions

The current quiz includes questions on:
- **Geography**: Capital cities
- **Programming**: Web development languages
- **Mathematics**: Basic arithmetic
- **Literature**: Classic authors

## Scoring System

- Each correct answer awards 1 point
- Your final score is displayed as: `score/total_questions`
- Performance feedback:
  - All correct: "Excellent! You got all the answers right!"
  - More than half correct: "Good job! You did well."
  - Half or less correct: "Better luck next time!"

## Customization

You can easily customize the quiz by modifying the `questions` dictionary in the `run_quiz()` function:

```python
questions = {
    "Your question here?": {
        "options": ["a) Option 1", "b) Option 2", "c) Option 3", "d) Option 4"],
        "answer": "b"  # Correct answer key
    }
}
```

## Future Enhancements

Potential improvements for future versions:
- Add more questions and categories
- Implement difficulty levels
- Store high scores
- Add timer functionality
- Include question randomization
- Support for different question types (true/false, fill-in-the-blank)
- Create a GUI version

## Contributing

Feel free to fork this project and submit pull requests with improvements or additional features. Some ideas:
- Add more questions
- Improve the user interface
- Add new question categories
- Implement a database for questions

## License

This project is open-source and available for educational purposes.

## Author

Created as an educational Python project to demonstrate:
- Dictionary data structures
- Loops and iteration
- Conditional statements
- User input handling
- String formatting

## Support

For issues, questions, or suggestions, please create an issue in the repository or contact the maintainer.

---

**Enjoy the quiz and happy learning!** 🎓
