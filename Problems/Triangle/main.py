height = int(input())

for i in range(height + 1):
    print(f"{' ' * (height - i)}{'#' * (2 * i - 1)}")
