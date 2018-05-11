# Break with Loop
some_list = ['name1','name2','name3','name4']

for i in some_list:
    if i == 'name3':
        print('Found name in list')
        break
    print('Test name: {}'.format(i))


# Exception Handling
student_dict = {'name': 'kevin',
           'student id': 21,
           'feedback': None}

# print(student['name'])


def find(student):

    first_name = student['name']

    try:
        last_name = student['last_name']
        # add_number_string = 3 + first_name

    except KeyError:
        last_name = 'Unknown'
        print('Error finding last_name')

    except TypeError as error:
        print('Cant add strings and integers together')
        print(error) # General Python Output Error

    print(first_name)
    print(last_name)
    # print(add_number_string)

    print('Code Ran Fine')


find(student_dict)