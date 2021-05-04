"""
DeptNameComparator
"""
class DeptNameComparator:
    def __init__(self):
        pass
    def compare(self, first, second):
        comparison = 0
        if first.getdeptname() < second.getdeptname():
            comparison = -1
        elif first.getdeptname() > second.getdeptname():
            comparison = 1
        else:
            comparison = 0
        return comparison
