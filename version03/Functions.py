# Seven (7) functions that provide logic for the options in main() menu.


from project_class import Project
import os
import copy
import atexit

# Initialize lists []
project_queue = []
project_list = []
project_completed = []

# file variables and values
file_info = "id,name,size,priority"
required_csv = "required.csv"
done_csv = "done.csv"


# Seven (7) File Handling functions

###############################################################################
def reader():
    """Function 1: File reader"""

    # Check if file "required.csv" exists
    if os.path.exists(required_csv):
        with open(required_csv, "r") as file:
            header = file.readline().rstrip()
            if header == file_info:
                for _line in file:
                    line = _line.split(",")

                    try:
                        # Create Project() class object instance
                        project = Project(
                            int(line[0]), line[1], int(line[2]), int(line[3]))
                        # Add the project to the project list

                        # Avoid duplicates
                        if project not in project_list:
                            project_list.append(project)
                    except ValueError as ve:
                        print(f"Bad value for line: {line}, skipping...")
                        print(f"Except: {ve}")

            else:
                print("Header not correct")
                file.close()

                # Rename the file to required.csv.bak
                if os.path.exists(required_csv + ".bak"):
                    os.remove(required_csv + ".bak")

                os.rename(required_csv, required_csv + ".bak")

                # Create a new file required.csv
                with open(required_csv, "w") as file:
                    # Write header
                    file.write(file_info + "\n")
                    file.close()

    else:
        # Create a new file required.csv
        with open(required_csv, "w") as file:
            # Write header
            file.write(file_info + "\n")
            file.close()

    # Check if done.csv file exists
    if os.path.exists(done_csv):
        with open(done_csv, "r") as file:
            # Verify if header is correct
            header = file.readline().rstrip()
            if header == file_info:
                # Read the file line by line
                for _line in file:
                    # Split  line by comma
                    line = _line.split(",")

                    try:
                        # Create a Project() class object instance
                        project = Project(int(line[0]), line[1], int(
                            line[2]), int(line[3]), True)
                        # add the project to the project list

                        # avoiding duplications
                        if project not in project_completed:
                            project_completed.append(project)
                    except ValueError as ve:
                        print(f"Bad value for line: {line}, skipping...")
                        print(f"Except: {ve}")
            else:
                print("The header is not correct")
                file.close()

                # rename the file to done.csv.bak
                if os.path.exists(done_csv + ".bak"):
                    os.remove(done_csv + ".bak")

                os.rename(done_csv, done_csv + ".bak")

                # create a new file done.csv
                with open(done_csv, "w") as file:
                    # write the header
                    file.write(file_info + "\n")
                    file.close()

    else:
        # create a new file done.csv
        with open(done_csv, "w") as file:
            # write the header
            file.write(file_info + "\n")
            file.close()


###############################################################################

def writer():
    """Function 2: File writer"""
    global project_list, project_completed

    for project in project_list:
        if project in project_completed:
            project_list.remove(project)

    # Write project_list to required_csv
    with open(required_csv, 'w') as csvfile:
        csvfile.write(file_info + '\n')
        for project in project_list:
            csvfile.write(str(project.id) + "," + str(project.title) + "," +
                          str(project.size) + "," + str(
                project.priority) + "\n")

    # Write project_completed to done_csv
    with open(done_csv, 'w') as csvfile:
        csvfile.write(file_info + '\n')
        for project in project_completed:
            csvfile.write(str(project.id) + "," + str(project.title) + "," +
                          str(project.size) + "," + str(
                project.priority) + "\n")


###############################################################################

def get_project():
    """Function 3: Get a Project"""
    global project_list, project_queue

    # check if queue is empty
    if len(project_queue) == 0:
        print("Project queue is empty, generate a queue first. (option 1)")
    else:
        # get a project from the top of the queue...
        proj = project_queue[0]

        # ...print its details...
        print("This will be your current project: " + str(proj))

        # ...confirm the project selection...
        user_input = input("Is this correct? ('y' or any key to cancel): ")
        if user_input == 'y':
            print("Marking project id " + str(proj.id) + " as complete.")
            proj.complete = True

            # ...pop the project from the queue...
            project_queue.pop(0)

            # ...remove the project from the project list...
            project_list.remove(proj)

            # ...and add it to the completed list
            project_completed.append(proj)
        else:
            # ...otherwise, confirm cancellation.
            print("Project selection cancelled.")

        # Print the queue
        print("Current Project queue: ")
        for project in project_queue:
            print(project)


###############################################################################

def schedule_project():
    """Function 4: Schedule Projects"""
    global project_queue

    print("1. Create Schedule"
          "\n2. View Schedule")

    user_input = input("\nEnter schedule menu choice: ")
    if user_input == '1':

        # check if the project list is empty
        if len(project_list) == 0:
            print("Project list is empty, please add projects first!")
        else:
            # create queue from project list
            project_queue = copy.deepcopy(project_list)

            # sort projects by priority first, then size
            project_queue.sort(key=lambda x: (x.priority, x.size, x.id))

            # print the queue
            print("Project queue created")
            print("Projects in queue: ")
            for project in project_queue:
                print(project)

    elif user_input == '2':
        # View Schedule
        # check if queue is empty
        if len(project_queue) == 0:
            print("Project queue is empty, generate a queue first.")
        else:
            # print the queue
            print("Current Project queue: ")
            for project in project_queue:
                print(project)

    else:
        print("Invalid Input, try again")


###############################################################################

def view_project():
    """Function 5: View Projects"""
    while True:
        print("1. One Project"
              "\n2. Completed Projects"
              "\n3. All Projects")

        user_input = input("\nEnter project menu choice: ")
        if user_input == '1':
            # One Project
            # Check if project list is empty
            if len(project_list) == 0:
                print("\tProject list is empty")
                break

            # get project id
            try:
                project_id = int(input("Enter project id: "))
            except ValueError as ve:
                print("Invalid ID Number, try again")
                print(f"Except: {ve}")
                continue

            # check if id exists
            if project_id in [project.id for project in
                              project_list + project_completed]:
                for project in project_list + project_completed:
                    if project.id == project_id:
                        print(project)
                        break
            else:
                print("Project not found")

        elif user_input == '2':
            # Completed Projects
            # Enumerate all projects that are complete
            print("\tProjects that are complete: ")
            if len(project_completed) == 0:
                print("\tNo complete projects")
            else:
                for project in project_completed:
                    print(project)

        elif user_input == '3':
            # All Projects
            # list all projects
            print("\tIncomplete projects: ")
            if len(project_list) == 0:
                print("\tNo projects in list")
            else:
                for project in project_list:
                    print(project)

            print("\n\tComplete projects: ")

            if len(project_completed) == 0:
                print("\tNo projects completed")
            else:
                for project in project_completed:
                    print(project)

        else:
            print("Invalid Input, try again")

        break


###############################################################################

def insert_project():
    """Function 6: Input Project Details aka New Project"""
    while True:

        try:
            # get project ID
            proj_id = int(input("\tEnter Project ID: "))
        except ValueError as ve:
            print("\tInvalid ID. Should be a number, please try again")
            print(f"\t(exception: {str(ve)})")
            continue

        # check if id exists in project_list
        if proj_id in [project.id for project in
                       project_list + project_completed]:
            print("\tID Number already exists, try again")
            continue

        # get project name
        proj_name = input("\tEnter Project Name: ")

        try:
            # get number of pages
            proj_size = int(input("\tEnter Number of Pages: "))
        except ValueError as ve:
            print(
                "\tInvalid number of pages (should be a number), please try "
                "again")
            print(f"\t(exception: {str(ve)})")
            continue

        # get priority
        try:
            proj_priority = int(input("\tEnter Priority: "))

            if int(proj_priority) <= 0:
                raise ValueError("\tPriority must be greater than 0")
        except ValueError as ve:
            print("\tInvalid Priority. Should be a number, please try again")
            print(f"\t(exception: {str(ve)})")
            continue

        # create project
        new_project = Project(proj_id, proj_name, proj_size, proj_priority)

        # add to list
        project_list.append(new_project)

        # print out confirmation
        print(f'\tProject "{new_project.title}" added to project list')

        # clear project queue (if not empty) and notify user
        if len(project_queue) != 0:
            project_queue.clear()
            print(
                "\tNote: Project queue cleared because a new project is "
                "added.")

        break


###############################################################################

def main():
    """Function 7: Main Menu"""

    # read the file
    reader()

    # Flag to act as a signal to the program
    active_run = True

    while active_run:

        # Menu with five (5) options
        print("============================")
        print("[1] Input Project Details"
              "\n[2] View Projects"
              "\n[3] Schedule Projects"
              "\n[4] Get a Project"
              "\n[5] Exit")
        print("============================")

        # Get user input
        user_input = input("\nEnter menu choice: ")

        # Input Project Details
        if user_input == '1':
            insert_project()

        # View Projects
        elif user_input == '2':
            view_project()

        elif user_input == '3':
            schedule_project()

        elif user_input == '4':
            get_project()

        elif user_input == '5':
            print("Exited")
            active_run = False

        else:
            print("Invalid Input, try again")

    # write the file
    writer()
