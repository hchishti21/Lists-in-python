
available_parts = ["Computer\n", "Monitor\n", "Mouse\n", "hdmi cable"]
valid_choices = []
# valid_choices = [str(i) for i in range (1, len(available_parts) +1)]
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = []
while current_choice != '0':
    if current_choice in valid_choices:
        print("Adding{}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
        if current_choice == '1':
            computer_parts.append("Computer")
        elif current_choice == '2':
            computer_parts.append("Monitor")
        elif current_choice == '3':
            computer_parts.append("Mouse")
        elif current_choice == '4':
            computer_parts.append("hdmi cable")
        else:
            print("0: to finish")
    else:
        print("Please add options from below list: ")
    for number, part in enumerate(available_parts):
        print("{0}, {1}".format(number + 1, part))
    current_choice = input()
print(computer_parts)

