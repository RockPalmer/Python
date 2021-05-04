"""
Sorts
"""
def sort(deptlist, xComparator):
    count1 = 0
    while count1 < len(deptlist):
        count2 = count1 + 1
        while count2 < len(deptlist):
            if xComparator.compare(deptlist[count1], deptlist[count2]) > 0:
                tempdept = deptlist[count1]
                deptlist[count1] = deptlist[count2]
                deptlist[count2] = tempdept
            count2 = count2 + 1
        count1 = count1 + 1
