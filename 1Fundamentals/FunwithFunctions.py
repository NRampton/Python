def odd_even(start, end):               # outputs each number, along with odd/even
    for count in range(start, end + 1):
        output = "Number is "
        output += str(count)
        if count % 2 == 0:
            output += ". This is an even number."
        else:
            output += ". This is an odd number."
        print output


# odd_even(1, 2000)

def multiply(lst, mult):            # each value of lst is multiplied by mult in place
    for count in range(len(lst)):
        lst[count] = mult * lst[count]
    return lst


# multiply([2,4,10,16], 4)

def layered_multiples(llist):           # multiplies lst by mult in multiply(), then
    new_list = []                       # returns a new list of lists with a number
    for count in range(len(llist)):     # of 1s equal to each index's value
        sub_list = []
        for count2 in range(llist[count]):
            sub_list.append(1)
        new_list.append(sub_list)
    return new_list


x = layered_multiples(multiply([2, 4, 10], 4))
print x
