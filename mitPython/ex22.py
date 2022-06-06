n = 12
print('Hello!')
for i in range(2 , n + 1, 2):
    n -= 2
    if n < 2:
        break
    else:
        print(n)