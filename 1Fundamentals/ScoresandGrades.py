import random


def scores(num):
    for count in range(num):
        score = random.randint(60, 100)
        if score <= 69:
            grade = "D"
        elif score <= 79:
            grade = "C"
        elif score <= 89:
            grade = "B"
        else:
            grade = "A"
        print "Score: {}; your grade is {}.".format(str(score), grade)


scores(10)
