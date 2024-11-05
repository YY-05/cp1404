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
