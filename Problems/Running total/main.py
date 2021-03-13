input_list = list(input())

input_list = [int(x) for x in input_list]

for i in range(1, len(input_list)):
    input_list[i] += input_list[i - 1]

print(input_list)
