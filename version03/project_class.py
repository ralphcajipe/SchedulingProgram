"""
A class that represents a project's ID, Title, Size, and Priority.
It marks the project as completed or incomplete.
"""


class Project:
    """Represent aspects of a Project with three (3) methods.
    NOTE: A function inside a class is called a `method`."""

    def __init__(self, id, title, size, priority, completed=False):
        """Method 1: Initialize attributes to describe a Project"""

        # Project ID input
        # This is only a weak warning by interpreter
        # Because it Shadows built-in name 'id'. Ignore warning.
        self.id = id

        # Project title input
        self.title = title

        # Project size input based on page number
        self.size = size

        """Project priority input. 
        The lower the number, the higher the priority."""
        self.priority = priority

        # Project completeness input
        self.completed = completed

    ###########################################################################
    def __str__(self):
        """Method 2: View a project's details"""
        return "\tID: " + str(self.id) \
               + ", Title: '" + self.title \
               + "', Size: " + str(self.size) \
               + ", Priority: " + str(self.priority) \
               + ", Completed: " + str(self.completed)

    ###########################################################################
    def __eq__(self, other):
        return self.id == other.id \
               and self.title == other.title \
               and self.size == other.size \
               and self.priority == other.priority \
               and self.completed == other.completed
