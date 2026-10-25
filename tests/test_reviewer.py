
import pytest

from app.reviewer import review_code


def test_review_code_accepts_source_code():
    result = review_code("print('Hello, world!')")

    assert result == (
        "Code received successfully. AI review is not implemented yet."
    )


def test_review_code_rejects_empty_source_code():
    with pytest.raises(ValueError, match="Source code cannot be empty."):
        review_code("   ")
