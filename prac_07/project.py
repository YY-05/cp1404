from datetime import datetime


class Project:
    """Represent information about a project."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a project from the given values."""
        self.name = name
        if isinstance(start_date, str):
            self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        else:
            self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def is_completed(self):
        """Determine if language is completely typed."""
        return self.completion_percentage == 100

    def __str__(self):
        """Return string representation of a Project."""
        start_date_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {start_date_str}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")
