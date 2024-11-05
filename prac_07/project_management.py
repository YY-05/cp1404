from project import Project
import datetime


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
    for project in filtered_projects:
        print(project)