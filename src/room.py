# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def display_items(self):
        if len(self.items) == 0:
            print('There are no items here.')
        else:
            print('You see here:')
            for item in self.items:
                print(item.name, item.description)
            print(
                'Do you wish to pick up an item? type: [grab] [item_name]')
