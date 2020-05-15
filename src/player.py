# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def move(self, command):
        room = getattr(self.current_room, f'{command}_to')
        # Print an error message if the movement isn't allowed.
        if room is None:
            print('As you were, Marine. Access denied! Pick a different direction.\n')
        # Prints the current room name and description.
        elif room is not None:
            self.current_room = room
            print('-----------------------------------------------------------------\n')
            print(f'{self.name} has entered the {self.current_room.name}\n')
            print(f'{self.current_room.description}\n')
            self.current_room.display_items()

    def grab_item(self, selected_item):
        for item in self.current_room.items:
            if item.name == selected_item:
                self.inventory.append(item)
                self.current_room.items.remove(item)
                print(f'You added {item.name} to your rucksack.\n')
            else:
                print('That item is not here.\n')

    def drop_item(self, selected_item):
        for item in self.inventory:
            if item.name == selected_item:
                self.inventory.remove(item)
                self.current_room.items.append(item)
                print(
                    f'You dropped {item.name} in the {self.current_room.name}.\n')
            else:
                print('You do not have that item.\n')

    def display_inventory(self):
        if len(self.inventory) == 0:
            print('Your rucksack is currently empty.\n')
        else:
            print("\nYour rucksack has: ")
            for item in self.inventory:
                print(item.name)
