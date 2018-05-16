#
# Break with Loop
#

# some_list = ['name1','name2','name3','name4']
#
# for i in some_list:
#     if i == 'name3':
#         print('Found name in list')
#         break
#     print('Test name: {}'.format(i))



#
# Exception Handling
#

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


#find(student_dict)


#
# Classes, Inheritance, Polymorphism
#

students = []

# Parent Class
class Student(object):

    school_name = 'Mark Twain Elementary'

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

# Child Class of Student
class HighSchoolStudent(Student):

    school_name = 'Carson High School'

    def get_school_name(self):
        return 'This is a High School student'

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + ' -HS'



# james = HighSchoolStudent('james')
# print(james.get_name_capitalize())
# print(james.get_school_name())