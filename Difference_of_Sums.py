n =int(input())
summ = 0
squares = 0
for i in range(1,n+1):
    summ += i
    squares += i**2
print(abs(squares - summ**2))
    