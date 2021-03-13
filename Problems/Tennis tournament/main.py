winners = []

for _ in range(int(input())):
    player = input().split()
    if player[1] == 'win':
        winners.append(player[0])

print(winners, len(winners), sep='\n')
