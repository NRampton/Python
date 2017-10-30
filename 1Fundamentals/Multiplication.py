print "x  1  2  3  4  5  6  7  8  9  10 12"
for f in range(1, 13):
    output = "{}  ".format(f)
    for e in range(1, 13):
        output += "{} ".format(e * f)
    print output
