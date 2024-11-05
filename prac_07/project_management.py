from project import Project
import datetime


def main():
    filename = "projects.txt"
    menu = """- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date
    - (A)dd new project)\n- (U)pdate project\n- (Q)uit"""
    print("Welcome to Pythonic Project Management")


def load_projects(filename):
    projects = []
    in_file = open(filename, "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    in_file.close()
    return projects


def save_projects(filename, projects):
    out_file = open(filename, "w")
    out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
    for project in projects:
        out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
        out_file.close()


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
    date_string = input("Show projects that start after date (dd/mm/yy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date >= date]
    filtered_projects = sorted(filtered_projects, key=lambda x: x.start_date)
    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ").title()
    start_date = input("Start date (d/m/yy): ")
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
