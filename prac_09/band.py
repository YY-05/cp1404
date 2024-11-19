class Band:
    def __init__(self, name):
        """Initialise a Band."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician."""
        self.musicians.append(musician)

    def play(self):
        """Returns a string showing the instrument that the musician play."""
        instrument = []
        for musician in self.musicians:
            instrument.append(musician.play())
        return '\n'.join(instrument)

    def __str__(self):
        """return the string"""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"
