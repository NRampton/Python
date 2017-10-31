import random


def tosses(num):
    print "Starting the program..."
    num_heads = 0
    num_tails = 0
    for count in range(num):
        flip = random.randint(0,1)
        if flip == 1:
            result = "heads"
            num_heads += 1
        elif flip == 0:
            result = "tails"
            num_tails += 1
        print "Attempt # {}: Throwing a coin... It's {}! That makes {} heads and {} tails so far!".format(str(count + 1), result, str(num_heads), str(num_tails))
    print "My thumb is sore."


tosses(5000)
