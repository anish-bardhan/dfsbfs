import random

#passengers = [[random.randint(0,100) for x in range(6)] for y in range(5)]

#monday = [random.randint(200,201) for x in range(5)]

#for day in range(len(monday)):
        #passengers[day][0] = monday[day]

#print(passengers)

passengers = [[0 + x for x in range(7)] for y in range(7)]

def total(arr):
    sum = 0
    for row in range(len(arr)):
        sum += arr[row][row]
    return sum

#print(total(passengers))

def d_total(arr):
    sum = 0
    col = 0
    for row in range(len(arr)):
        while col < len(arr):
            sum += arr[row][col]
            col += 1
    return sum

print(d_total(passengers))

def i_total(arr):
    sum = 0
    col = len(arr)
    for row in range(len(arr)):
        while col > 0:
            col -= 1
            sum += arr[row][col]
    return sum
print(passengers)
print(i_total(passengers))
