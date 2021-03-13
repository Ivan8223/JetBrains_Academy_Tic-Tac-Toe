num_list = []

while True:
    number = input()
    if number == '.':
        break
    num_list.append(float(number))

print(min(num_list))
