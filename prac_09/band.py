class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        instrument = []
        for musician in self.musicians:
            instrument.append(musician.play())
        return '\n'.join(instrument)