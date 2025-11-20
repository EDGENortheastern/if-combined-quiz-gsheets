import random # to generate random values


def generate_question() -> tuple[int, int, int]:
    """
    Return (num1, num2, correct_answer) for a times tables question.
    """
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    return num1, num2, num1 * num2
