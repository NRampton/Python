lst = ["hello", "there", "you", "awesome", "dude"]
hasstring = False
hasint = False
final_string = ""
final_sum = 0

for count in lst:
    if isinstance(count, int):
        hasint = True
        final_sum += count
    elif isinstance(count, str):
        hasstring = True
        final_string += " " + count
if hasstring and hasint:
    print "The list you entered is of mixed type"
    print "String:" + final_string
    print "Sum:", str(final_sum)
elif hasstring:
    print "The list you entered is of string type"
    print "String:" + final_string
elif hasint:
    print "The list you entered is of integer type"
    print "Sum:", str(final_sum)
