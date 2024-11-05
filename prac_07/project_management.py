from project import Project
import datetime


def main():
    filename = "projects.txt"
    menu = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")
    while True:
        print(menu)
        choice = input(">>> ").lower()
        if choice not in ["l", "s", "d", "f", "a", "u", "q"]:
            print("Invalid choice")
        elif choice == "l":
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "s":
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            whether_save = input("Would you like to save to projects.txt? ").lower()
            if whether_save.startswith("y"):
                save_projects(filename, projects)
                print("Projects saved.")
            print("Thank you for using custom-built project management software.")
            break


def load_projects(filename):
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    return projects


def save_projects(filename, projects):
    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    incomplete = sorted([project for project in projects if not project.is_completed()], key=lambda x: x.priority)
    print("Incomplete projects: ")
    for project in incomplete:
        print(f"  {project}")
    complete = sorted([project for project in projects if project.is_completed()], key=lambda x: x.priority)
    print("Completed projects:")
    for project in complete:
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")  # e.g., "30/09/2022"
    try:
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please enter date in dd/mm/yyyy format.")
        return
    filtered_projects = [project for project in projects if project.start_date >= date]
    filtered_projects = sorted(filtered_projects, key=lambda x: x.start_date)
    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ").title()
    start_date_string = input("Start date (d/m/yyyy): ")
    start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    while True:
        project_choice = input("Project choice: ")
        if not project_choice.isdigit():
            print("Invalid input, please enter a number.")
            continue
        project_choice = int(project_choice)
        if project_choice < 0 or project_choice >= len(projects):
            print("Invalid input, please enter a valid project number.")
            continue
        print(projects[project_choice])
        break
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_percentage:
        projects[project_choice].completion_percentage = int(new_percentage)
    if new_priority:
        projects[project_choice].priority = int(new_priority)


main()
