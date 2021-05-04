"""
Assignment2
"""
num = ""
nums = list()
stopper = 0
# Continue to read input until a line is found containing '0'
while stopper == 0:
    numString = input("")
    hasNumber = 0
    count = 0
    while count < len(numString) and stopper == 0:
        if numString[count].isnumeric() or numString[count] == "-":
            num = num + str(numString[count])
            hasNumber = 1
        elif num == "0":
            stopper = 1
        elif hasNumber == 1:
            nums.append(int(num))
            num = ""
            hasNumber = 0
        count = count + 1
    if hasNumber == 1:
        if num != "0":
            nums.append(int(num))
        else:
            stopper = 1
        hasNumber = 0
        num = ""
maxint = nums[0]
count = 1
while count < len(nums):
    if nums[count] > maxint:
        maxint = nums[count]
    count = count + 1
evennumcount = 0
count = 0
while count < len(nums):
    if nums[count] % 2 == 0:
        evennumcount = evennumcount + 1
    count = count + 1
firstoddint = 0
stopper = 0
count = 0
while stopper == 0 and count < len(nums):
    if nums[count] % 2 != 0:
        stopper = 1
        firstoddint = nums[count]
    count = count + 1
smallestoddint = firstoddint
count = 0
while count < len(nums):
    if nums[count] % 2 != 0:
        if nums[count] < smallestoddint:
            smallestoddint = nums[count]
    count = count + 1
sumnegints = 0
count = 0
while count < len(nums):
    if nums[count] < 0:
        sumnegints = sumnegints + nums[count]
    count = count + 1
print("The maximum integer is " + str(maxint))
print("The count of even integers in the sequence is " + str(evennumcount))
print("The smallest odd integer in the sequence is " + str(smallestoddint))
print("The sum of negative integers is " + str(sumnegints))
    
