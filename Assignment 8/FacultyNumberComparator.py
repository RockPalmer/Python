"""
FacultyNumberComparator
"""
class FacultyNumberComparator:
    def __init__(self):
        pass
    def compare(self, first, second):
        return (first.getnumofmembers() - second.getnumofmembers())
