bio_dictionary = {}
bio_dictionary['name'] = "Nick"
bio_dictionary['game'] = 'coding like a mofo'
bio_dictionary['age'] = 37
bio_dictionary['country'] = "the USA"
bio_dictionary['lang'] = 'Russian'


def print_bio(dict):
    print "{}'s my name, and".format(dict['name'])
    print "{}'s my game.".format(dict['game'])
    print "I'm {} years old.".format(dict['age'])
    print "I was born in {}.".format(dict['country'])
    print "My favorite language is {}.".format(dict['lang'])


print_bio(bio_dictionary)
