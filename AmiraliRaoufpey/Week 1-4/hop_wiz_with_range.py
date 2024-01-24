limit = int(input('enter the game limit: '))

for num in range(1, limit):
    decision = 'HopWiz' if num in range(0, limit, 21) else 'Hop' if num in range(0, limit, 3) \
        else 'Wiz' if num in range(0, limit, 7) else str(num)
    print(decision)
