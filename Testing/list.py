def main():
    my_file = open("super_villains.txt")

    name_list = []
    for line in my_file:
        line = line.strip()
        name_list.append(line)

    my_file.close()

    print(name_list)
    print("there were", len(name_list), "names on the file.")

# liner search
    key = "Octavia the Siren"

    current_list_position = 0
    while current_list_position < len(name_list) and name_list[current_list_position] != key:
        current_list_position += 1

    if current_list_position < len(name_list):
        print("found at", current_list_position)
    else:
        print("not found")


    key = "Severin de Helborne"

    lower_bound = 0
    found = False
    upper_bound = len(name_list) - 1
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2

        if name_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        if name_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True

        if found:
            print("the name is at position", middle_pos)

        else:
            print("name not found")


            # log2(n)
#             test answer



main()