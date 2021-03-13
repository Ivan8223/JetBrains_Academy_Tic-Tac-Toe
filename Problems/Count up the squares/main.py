# put your python code here
numbers = []
squares = []

while True:
    input_number = int(input())
    numbers.append(input_number)
    squares.append(input_number ** 2)
    if sum(numbers) == 0:
        print(sum(squares))
        break
