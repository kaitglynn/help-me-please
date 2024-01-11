```python
import random

class TestGenerator:
    def __init__(self, question_bank):
        self.question_bank = question_bank

    def generate_test(self, num_questions):
        test_questions = random.sample(self.question_bank, num_questions)
        return test_questions

# Example usage:
# question_bank = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"]
# test_gen = TestGenerator(question_bank)
# print(test_gen.generate_test(5))
```