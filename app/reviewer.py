
import ollama


MODEL_NAME = "llama3.2:3b"


def review_code(source_code: str) -> str:
    """Review source code using a locally running Ollama model."""

    if not source_code.strip():
        raise ValueError("Source code cannot be empty.")

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an experienced software code reviewer. "
                    "Analyze the submitted source code for potential bugs, "
                    "security vulnerabilities, and code-quality issues. "
                    "Explain your findings clearly. If you find no issues, "
                    "say so, while noting that the review is not exhaustive."
                ),
            },
            {
                "role": "user",
                "content": f"Review this source code:\n\n{source_code}",
            },
        ],
    )

    return response["message"]["content"]
