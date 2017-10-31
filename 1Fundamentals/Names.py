students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def names_one(lst):
    for count in range(len(lst)):
        print lst[count]['first_name'], lst[count]['last_name']


# names_one(students)

users = {
    'Students': [
        {'first_name': 'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
}


def names_two(dict):
    print "Students"
    for count in range(len(dict['Students'])):
        output = ""
        output += str(count + 1) + " - "
        output += dict['Students'][count]['first_name'] + " "
        output += dict['Students'][count]['last_name'] + " - "
        output += str(len(dict['Students'][count]['first_name']) + len(dict['Students'][count]['last_name']))
        print output
    print "Instructors"
    for count in range(len(dict['Instructors'])):
        output = ""
        output += str(count + 1) + " - "
        output += dict['Instructors'][count]['first_name'] + " "
        output += dict['Instructors'][count]['last_name'] + " - "
        output += str(len(dict['Instructors'][count]['first_name']) + len(dict['Instructors'][count]['last_name']))
        print output


names_two(users)
