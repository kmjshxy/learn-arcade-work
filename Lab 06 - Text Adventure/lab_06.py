class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []

    living_room = Room("You are in a living room, its cute you can see the kitchen to the south."
                       " You can go to the north, south, or west!", 1, None, 3, 9)
    room_list.append(living_room)

    n_porch = Room(" You are on the north side of the porch, there are some wind chimes making sound. "
                   " You can go south or east to the other side of the porch!", None, 2, 0, None)
    room_list.append(n_porch)

    e_porch = Room("You are on the east side of the porch, there are some chairs for people to sit on."
                   " You can go south or north to the other side of the porch! ", None, None, 4, 1)
    room_list.append(e_porch)

    kitchen = Room("You are in a kitchen, it smells like spices you can see the living room to the north!"
                   " You can go in any direction!", 0, 4, 8, 6)
    room_list.append(kitchen)

    garage = Room("You are in a garage, there is a lot of stuff!"
                  " You can go north, south, or west", 2, None, 5, 3)
    room_list.append(garage)

    stairs = Room(" You are in a room with stairs to a basement,"
                  " they look a bit scary so you feel like you should go back north to the garage! ", 4, None, None, None)
    room_list.append(stairs)

    bedroom_1 = Room("You are in a bedroom, its a bit messy!"
                     " You can go north, east, or south.", 9, 3, 7, None)
    room_list.append(bedroom_1)

    study = Room("You are in study, it looks like someone has been working hard!"
                 " You can go north or east.", 6, 8, None, None)
    room_list.append(study)

    bedroom_2 = Room("You are in a bedroom, it looks super clean, like it has not been used in a while."
                     " You can go north or west.", 3, None, None, 7)
    room_list.append(bedroom_2)

    bathroom = Room("You are in a bathroom, it smells like air freshener!"
                    " You can go east or south", None, 0, 6, None)
    room_list.append(bathroom)

    current_room = 0
    print(room_list[current_room].description)
    done = False
    while not done:
        print()
        choice= input("where would you like to go next?")
        if choice.lower() == "n" or choice.lower() == "north":
            next_room = room_list[current_room].north
            if next_room == None:
                print("you cant go this way!!")
            else:
                current_room = next_room
        elif choice.lower() == "e" or choice.lower() == "east":
            next_room = room_list[current_room].east
            if next_room == None:
                print("you cant go this way!!")
            else:
                current_room = next_room
        elif choice.lower() == "s" or choice.lower() == "south":
            next_room = room_list[current_room].south
            if next_room == None:
                print("you cant go this way!!")
            else:
                current_room = next_room
        elif choice.lower() == "w" or choice.lower() == "west":
            next_room = room_list[current_room].west
            if next_room == None:
                print("you cant go this way!!")
            else:
                current_room = next_room
        else:
            print("where are you trying to go? try using n, e, s, w!!"
                  " If you want to quit type in quit ")

        print()
        print(room_list[current_room].description)

        if choice.lower() == "quit":
            done = True
            print()
            print("Goodbye!!")










main()

