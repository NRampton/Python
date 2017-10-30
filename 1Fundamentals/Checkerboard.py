char = "*"
output = ""
onoff = True
for val in range(8):
    for val in range(8):
        if onoff:
            output += char
            onoff = False
        else:
            output += " "
            onoff = True
    if onoff:
        onoff = False;
    else:
        onoff = True;
    output += "\n"
print output
