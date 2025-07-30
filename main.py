
with open("./Input/Letters/starting_letter.txt") as data:
    letter = data.read()
# print(letter)

with open("./Input/Names/invited_names.txt") as data:
    names = data.read()
# print(names)


def string_to_list(input_string):
    member_list = [member.strip() for member in input_string.split('\n')]
    return member_list


list_of_names = string_to_list(names)
# print(list_of_names)


def create_letters():
    for n in range(0, len(list_of_names) - 1):
        new_letter = letter.replace("[name]", list_of_names[n])
        with open(f"./Output/ReadyToSend/{list_of_names[n]}.txt", "w") as data1:
            data1.write(new_letter)


create_letters()
