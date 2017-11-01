name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def makeDict(list1, list2):
    if len(list1) > len(list2) or len(list1) == len(list2):
        key_list = list1
        val_list = list2
    else:
        key_list = list2
        val_list = list1
    print key_list
    print val_list
    zipped = zip(key_list, val_list)
    print zipped
    new_dict = dict(zipped)
    print new_dict
    return new_dict


makeDict(name, favorite_animal)
