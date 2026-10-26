
from unittest.mock import patch

import pytest

from app.models import CodeReview
from app.reviewer import review_code


@patch("app.reviewer.ollama.chat")
def test_review_code_returns_structured_findings(mock_chat):
    mock_chat.return_value = {
        "message": {
            "content": (
                '{"summary": "One bug found", '
                '"findings": [{'
                '"category": "bug", '
                '"severity": "high", '
                '"description": "Possible division by zero", '
                '"suggestion": "Check whether the divisor is zero"'
                '}]}'
            )
        }
    }

    result = review_code("def divide(a, b): return a / b")

    assert isinstance(result, CodeReview)
    assert result.summary == "One bug found"
    assert len(result.findings) == 1
    assert result.findings[0].category == "bug"
    assert result.findings[0].severity == "high"
    mock_chat.assert_called_once()


def test_review_code_rejects_empty_source_code():
    with pytest.raises(ValueError, match="Source code cannot be empty."):
        review_code("   ")


@patch("app.reviewer.ollama.chat")
def test_review_code_rejects_invalid_json(mock_chat):
    mock_chat.return_value = {
        "message": {
            "content": "This is not valid JSON"
        }
    }

    with pytest.raises(ValueError):
        review_code("print('hello')")
