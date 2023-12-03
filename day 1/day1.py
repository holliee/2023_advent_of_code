""" 
# part 1

# create sum
sum = 0
test = ""

def getNumber(num):
    for first in num:
        print(first)
        if (first.isnumeric()):
            test = first
            break;
    for second in reversed(num):
        print(second)
        if (second.isnumeric()):
            test += second
            break;   
    print(test)
    total = int(test)
    test = ""
    return total
        
# add up all numbers

# read in all lines
f = open("day_1.txt", "r")
for x in f:
  
  sum += getNumber(x)
f.close()
# print total
print("Sum: " + str(sum))

 """

# part 2

with open('day_1.txt') as file:
    lines = file.read().strip().split('\n')

total_value = 0

spelled_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


for line in lines:
    #print("BEFORE: "+ line)
    for i in range(len(spelled_numbers)):
        if spelled_numbers[i] in line:
            # need first and last letter incase it is part of another number
            line = line.replace(spelled_numbers[i], spelled_numbers[i][0]+str(i+1) + spelled_numbers[i][-1])
            #print("AFTER: "+ line)

    calibration_value = ''
    for i in range(len(line)):
        if line[i].isdigit():
            calibration_value+= line[i]
            break
    for i in range(len(line)):
        if line[len(line)-i-1].isdigit():
            calibration_value += line[len(line)-i-1]
            break
    total_value += int(calibration_value)
print(total_value)
file.close()