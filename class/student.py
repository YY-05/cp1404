# TEETH = 16
#
# monsters = [["Mike", 340, "blue"], ["James", 14, "green"], ["Randall", 24, "purple"]]
# scary_monsters = [monster for monster in monsters if monster[1] > TEETH]
# print(scary_monsters)


class Student:
def __init__(self, first_name="", last_name="", student_id=0):
self.first_name = first_name
self.last_name = last_name
self.id = student_id

def __str__(self):
return f"{self.first_name} {self.last_name} ({self.id})"