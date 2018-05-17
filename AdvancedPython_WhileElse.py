# While-Else Control Flow
# Favorite keyboard shortcut: Ctrl+Cmd+G highlights all occurrences of word for editing

some_list = [1,2,3,4]

while some_list:  # while True (while some_list is not empty this is true)
    print([i for i in some_list])
    some_list.pop()
else:
    print('Iteration Done')