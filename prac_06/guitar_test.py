from prac_06.guitar import Guitar


def test_age_and_vintage():
    """test the get_age() and is_vintage()"""
    guitar1 = Guitar("Gibson L-5 CES", 1922)
    guitar2 = Guitar("Another Guitar", 2013)
    print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age()}")
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")


test_age_and_vintage()
