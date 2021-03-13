number = int(input())

for i in range(2, number):
    if number % i == 0:
        print("This number is not prime")
        break
else:
    print(f"This number is "
          f"{'prime' if number > 1 else 'not prime'}")
