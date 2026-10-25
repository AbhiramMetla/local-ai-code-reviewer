
from unittest.mock import patch

import pytest

from app.reviewer import review_code


@patch("app.reviewer.ollama.chat")
def test_review_code_returns_ai_response(mock_chat):
    mock_chat.return_value = {
        "message": {
            "content": "Potential bug: division by zero."
        }
    }

    result = review_code("def divide(a, b): return a / b")

    assert result == "Potential bug: division by zero."
    mock_chat.assert_called_once()


def test_review_code_rejects_empty_source_code():
    with pytest.raises(ValueError, match="Source code cannot be empty."):
        review_code("   ")
