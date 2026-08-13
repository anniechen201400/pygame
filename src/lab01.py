"""Lab 01 public functions.

Implement the published contract without changing the function names or
parameters. Keep this module free of input(), print(), files, and UI code.
"""


def classify_score(score: int) -> str:
    """Return ``red``, ``amber``, or ``green`` for a score from 0 to 100."""
    x = isinstance(score, bool)
    if x :
        raise TypeError

    y = isinstance(score, int)
    if y == False:
        raise TypeError
  
    if score < 0 or score > 100:
         raise ValueError

    elif 0 <= score <= 59:
         return "red"

    elif 60 <= score <= 79:
         return "amber"

    elif 80 <= score <= 100:
         return "green"
    


def format_student_record(name: str, score: int) -> str:
    """Return ``<trimmed name> | <score> | <classification>``."""
    x = isinstance(name, str)
    if not x:
        raise TypeError

    name = name.strip()
    if name == "":
        raise ValueError

    classification = classify_score(score)
    return f"{name} | {score} | {classification}"