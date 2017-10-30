for val in range(100,100001):
    checker = False
    counter = 0
    counter2 = 0
    for i in range(2, val):
        counter += 1
        if val % i == 0:
            break
        elif counter == (val - 2):
            print "Foo - " + str(val)
            checker = True
    for j in range(2, val):
        if j * j != val:
            continue
        elif j * j == val:
            print "Bar - " + str(val)
            checker = True
    if not checker:
        print "FooBar - " + str(val)
