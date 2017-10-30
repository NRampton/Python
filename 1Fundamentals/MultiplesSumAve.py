for val in range(1, 1001):          # Printing vals from 1 to 1000
    print val

for val in range(5, 1000005, 5):    # printing from 5 to 1mil by fives
    print val

a = [1, 2, 5, 10, 255, 3]


sum = 0             # Finding the sum of the values in a list
for val in a:
    sum += val
print sum

sum = 0             # Finding the average of values in a list
for val in a:
    sum += val
ave = sum / len(a)
print ave
