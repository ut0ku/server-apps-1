from pydantic import BaseModel, field_validator, Field
import re

class User(BaseModel):
    name: str
    id: int

class UserWithAge(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator("message")
    def validate_bad_words(cls, v):
        bad_words = ["кринж", "рофл", "вайб"]
        pattern = r"\b(" + "|".join(bad_words) + r")\b"
        if re.search(pattern, v, flags=re.IGNORECASE):
            raise ValueError("Использование недопустимых слов")
        return v