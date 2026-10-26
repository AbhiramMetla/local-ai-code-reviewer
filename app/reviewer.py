
import ollama

from app.models import CodeReview


MODEL_NAME = "llama3.2:3b"


def review_code(source_code: str) -> CodeReview:
    """Review source code and return structured findings."""

    if not source_code.strip():
        raise ValueError("Source code cannot be empty.")

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an experienced Python code reviewer. "
                    "Inspect the submitted code for bugs, security issues, "
                    "and code-quality problems. "
                    "Check edge cases and possible runtime exceptions. "
                    "For division operations, check whether the divisor "
                    "could be zero. "
                    "For every concrete issue, provide a finding with a "
                    "valid category, severity, description, and suggestion. "
                    "Do not invent issues unsupported by the code. "
                    "Return valid JSON with exactly these top-level keys: "
                    '"summary" and "findings". '
                    "Each finding must contain category, severity, "
                    "description, and suggestion. "
                    "If a concrete issue is found, include it in findings."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Review this Python code:\n\n"
                    f"{source_code}\n\n"
                    "Return a summary and all concrete findings, "
                    "with a practical fix for each issue."
                ),
            },
        ],
        format="json",
    )

    return CodeReview.model_validate_json(
        response["message"]["content"]
    )
