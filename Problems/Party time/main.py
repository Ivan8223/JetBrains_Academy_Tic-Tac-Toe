guests_list = []

while True:
    guest_name = input()
    if guest_name == '.':
        break
    guests_list.append(guest_name)

print(guests_list, len(guests_list), sep='\n')
