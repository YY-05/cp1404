import datetime


class Project:
    """Represent information about a Project."""

    def __init__(self, name, typing, reflection, pointer_arithmetic, year):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.pointer_arithmetic = pointer_arithmetic
        self.year = year

    def __repr__(self):
        """return a string"""
        return f"{self.name}, start: {self.start_date}, priority: {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"
