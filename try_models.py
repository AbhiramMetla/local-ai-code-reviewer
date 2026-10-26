
from app.models import CodeReview, ReviewFinding


finding = ReviewFinding(
    category="bug",
    severity="high",
    description="The function may divide by zero.",
    suggestion="Check whether the divisor is zero.",
)

review = CodeReview(
    summary="One potential bug was identified.",
    findings=[finding],
)

print(review.model_dump_json(indent=2))
