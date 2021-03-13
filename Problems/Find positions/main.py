seq = input().split()
num = input()
position = [str(i) for i, k in enumerate(seq) if k == num]
print(' '.join(position) if position else 'not found')
