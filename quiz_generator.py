```python
import random

class QuizGenerator:
    def __init__(self):
        self.quiz_database = self.load_quiz_database()

    def load_quiz_database(self):
        # Load the quiz database from a file or a database
        # This is a placeholder, replace with actual loading code
        return []

    def generate_quiz(self, topic, difficulty, num_questions):
        # Filter the questions based on the topic and difficulty
        questions = [q for q in self.quiz_database if q['topic'] == topic and q['difficulty'] == difficulty]

        # If there are not enough questions, return an error message
        if len(questions) < num_questions:
            return "Not enough questions in the database for this topic and difficulty."

        # Randomly select the questions
        selected_questions = random.sample(questions, num_questions)

        # Format the quiz
        quiz = "\n".join([self.format_question(q) for q in selected_questions])

        return quiz

    def format_question(self, question):
        # Format the question string
        # This is a placeholder, replace with actual formatting code
        return f"{question['question']} (Answer: {question['answer']})"

quiz_generator = QuizGenerator()
print(quiz_generator.generate_quiz("Python", "Easy", 10))
```