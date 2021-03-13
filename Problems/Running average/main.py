input_list = [int(num) for num in input()]

print([(input_list[i] + input_list[i + 1]) / 2 for i in range(len(input_list) - 1)])
