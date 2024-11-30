class User:

    def __init__(self, name):
        self.name = name
        self.number_of_tacos = 5
        self.score = 0

    def give_taco(self, other_user):
        if self.number_of_tacos > 0:
            self.number_of_tacos -= 1
            other_user.score += 1
        else:
            print(f"{self.name} has no tacos left to give!")

    def __str__(self):
        return f"{self.name}, {self.score} points, {self.number_of_tacos} tacos left"


users = []
user1 = User("Bob")
user = User("Alice")
print(user)
print(user.name)
print(user.number_of_tacos)
print(user.score)
users.append(user)
