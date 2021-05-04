"""
DeptFacultyComparator
"""
class DeptFacultyComparator:
    def __init__(self):
        pass
    def compare(self, first, second):
        comparison = 0

        # Compare last names
        if first.getfaculty().getlastname() < second.getfaculty().getlastname():
            comparison = -1
        elif first.getfaculty().getlastname() > second.getfaculty().getlastname():
            comparison = 1
        else:
            comparison = 0

        # Compare first names if last names are the same
        if comparison == 0:
            if first.getfaculty().getfirstname() < second.getfaculty().getfirstname():
                comparison = -1
            elif first.getfaculty().getfirstname() > second.getfaculty().getfirstname():
                comparison = 1
            else:
                comparison = 0
        return comparison
