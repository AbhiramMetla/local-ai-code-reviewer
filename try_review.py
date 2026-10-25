
from app.reviewer import review_code


sample_code = """
def divide(a, b):
    return a / b
"""

result = review_code(sample_code)

print("AI Code Review Result:")
print(result)
