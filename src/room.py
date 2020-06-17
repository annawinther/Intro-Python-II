# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, n_to = 0, e_to = 0, w_to = 0, s_to = 0, items = None ):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.w_to = w_to
        self.s_to = s_to
        self.items = items

# confirm if its there or not 
    def __str__(self):
        if self.items == None:
            return f' No items in {self.name} '
        else:
            output = ''
            output += self.name + '\n'
            item_number = 1
            for i in self.items:
                output =+ f' {item_number} {i.name}'
                item_number += 1


# get the input from user
# split by spaces - get an array of user commands
# command 1 must be in ['get', 'drop', 'go']
# if command[0] == 'get' : itemname = command[1]
