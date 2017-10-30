words = "It's thanksgiving day. It's my birthday, too!"     # finding and replacing
print words.find("day")
new_string = words.replace("day", "month")
print words

x = [2, 54, -2, 7, 12, 98]                      # finding min and max values
print min(x)
print max(x)

y = ['hello', 2, 54, -2, 7, 12, 98, 'world']        # making new list with first and
print y[0]                                          # last values of old list
print y[len(y)-1]
new_list = []
new_list.append(y[0])
new_list.append(y[len(y)-1])
print new_list

x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, -6]      # sorting, splitting, re-inserting
x = sorted(x)
y = x[:len(x)/2]
z = x[len(x)/2:]
z.insert(0, y)
print z
