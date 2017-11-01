my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}


def tupOut(dict):
    output = []
    for key, data in dict.items():
        output.append((key, data))
    print output


tupOut(my_dict)
