some_list = ['name1','name2','name3','name4']

for i in some_list:
    if i == 'name3':
        print('Found name in list')
        break
    print('Test name: {}'.format(i))