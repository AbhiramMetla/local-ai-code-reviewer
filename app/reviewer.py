
"""Core logic for the Local AI Code Review Assistant."""


def review_code(source_code: str) -> str:
    """Review source code and return review feedback."""
    if not source_code.strip():
        raise ValueError("Source code cannot be empty.")

    # AI review logic will be implemented in a later step.
    return "Code received successfully. AI review is not implemented yet."
