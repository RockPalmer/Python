"""
DeptManagement
"""
from Department import Department
from DeptNameComparator import DeptNameComparator
from FacultyNumberComparator import FacultyNumberComparator
from DeptFacultyComparator import DeptFacultyComparator
from Sorts import sort
class DeptManagement:
    def __init__(self):
        self.deptlist = list()
    def deptexists(self, deptname, universityname):
        deptindex = -1
        count = 0
        while count < len(self.deptlist) and deptindex == -1:
            thisdept = self.deptlist[count]
            if (thisdept.getdeptname() == deptname) and (thisdept.getuniversity() == universityname):
                deptindex = count
            count = count + 1
        return deptindex
    def facultyexists(self, firstname, lastname, academiclevel):
        facindex = -1
        count = 0
        while count < len(self.deptlist) and facindex == -1:
            thisfac = self.deptlist[count].getfaculty()
            if thisfac.getfirstname() == firstname and thisfac.getlastname() == lastname and thisfac.getacademiclevel == academiclevel:
                facindex = count
            count = count + 1
        return facindex
    def adddepartment(self, deptname, university, numofmembers, firstname, lastname, academiclevel):
        deptadded = True
        count = 0
        while count < len(self.deptlist) and deptadded:
            thisdept = self.deptlist[count]
            if thisdept.getdeptname() == deptname and thisdept.getuniversity() == university:
                deptadded == False
            count = count + 1
        else:
            if deptadded:
                newdep = Department(deptname, university, numofmembers, firstname, lastname, academiclevel)
                self.deptlist.append(newdep)
        return deptadded
    def removedepartment(self, deptname, universityname):
        deptremoved = False
        if self.deptexists(deptname, universityname) != -1:
            del self.deptlist[self.deptexists(deptname, universityname)]
            deptremoved = True
        return deptremoved
    def sortbydepartmentname(self):
        deptnamecomp = DeptNameComparator()
        sort(self.deptlist, deptnamecomp)
    def sortbyfacultynumbers(self):
        facnumcomp = FacultyNumberComparator()
        sort(self.deptlist, facnumcomp)
    def sortbydeptfaculty(self):
        deptfaccomp = DeptFacultyComparator()
        sort(self.deptlist, deptfaccomp)
    def listdepartments(self):
        thislist = "\nNo Department\n"
        outstring = "\n"
        if len(self.deptlist) != 0:
            count = 0
            while count < len(self.deptlist):
                outstring = outstring + str(self.deptlist[count])
                count = count + 1
        else:
            outstring = thislist
        return (outstring + "\n")
    def closedeptmanagement(self):
        self.deptlist.clear()
