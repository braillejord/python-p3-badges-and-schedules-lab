def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    name_list = [f"Hello, my name is {name}." for name in names]
    return name_list


def assign_rooms(names):
    room_list = []

    for index, item in enumerate(names):
        room_list.append(f"Hello, {item}! You'll be assigned to room {index + 1}!")

    return room_list


def printer(names):
    name_list = batch_badge_creator(names)
    for name in name_list:
        print(name)

    room_list = assign_rooms(names)
    for assignment in room_list:
        print(assignment)
