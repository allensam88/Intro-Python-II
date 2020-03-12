# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def switch_rooms(self, coordinate):
        room = getattr(self.current_room, f'{coordinate}_to')
        # Print an error message if the movement isn't allowed.
        if room is None:
			print("As you were, Marine. Access denied! Pick a different direction.")
        # Prints the current room name and description.
		elif room is not None:
            self.current_room = room
            print(f'{self.name} has entered the', self.current_room.name)
            print(self.current_room.description)
