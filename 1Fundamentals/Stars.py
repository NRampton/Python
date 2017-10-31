def draw_stars(x):                                  # prints out one line for each
    for count in range(len(x)):                     # value in x: int *s if it's an int,
        if isinstance(x[count], int):               # or the first char of str, len(str)
            output = ''                             # times
            for count2 in range(x[count]):
                output += "*"
            print output
        elif isinstance(x[count], str):
            first_char = x[count][0].lower()
            output = ''
            for count2 in range(len(x[count])):
                output += first_char
            print output


draw_stars([3, 4, 'Howdy!'])
