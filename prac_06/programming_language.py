class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __int__(self, name, typing, reflection, year):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
