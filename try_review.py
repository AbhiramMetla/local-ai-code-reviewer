
from app.reviewer import review_code


sample_code = """
def divide(a, b):
    return a / b
"""

review = review_code(sample_code)

print(review.model_dump_json(indent=2))
