# input
word_list = ['hello','world','my','name','is','Anna']
char = 'n'
# output
new_list = []
for val in range(len(word_list)):
    if word_list[val].find(char) > -1:
        new_list.append(word_list[val])
print new_list
