
from typing import Literal

from pydantic import BaseModel, Field, field_validator


class ReviewFinding(BaseModel):
    """Represents one issue identified during code review."""

    category: Literal["bug", "security", "code_quality"] = Field(
        description="Type of issue found"
    )

    severity: Literal["low", "medium", "high", "critical"] = Field(
        description="Severity of the issue"
    )

    description: str = Field(
        description="Explanation of the identified issue"
    )

    suggestion: str = Field(
        description="Recommended way to fix or improve the code"
    )

    @field_validator("category", mode="before")
    @classmethod
    def normalize_category(cls, value):
        """Normalize common category names returned by the AI."""

        if not isinstance(value, str):
            return value

        value = value.strip().lower().replace(" ", "_")

        aliases = {
            "performance": "code_quality",
            "code_smells": "code_quality",
            "code_smell": "code_quality",
        }

        return aliases.get(value, value)

    @field_validator("severity", mode="before")
    @classmethod
    def normalize_severity(cls, value):
        """Normalize severity capitalization."""

        if not isinstance(value, str):
            return value

        return value.strip().lower()


class CodeReview(BaseModel):
    """Represents the complete code review result."""

    summary: str = Field(
        description="Short summary of the code review"
    )

    findings: list[ReviewFinding] = Field(
        description="List of issues found in the submitted code"
    )
