def iseven(n):
    if n%2==0:
        return True
    else:
        return False
s = int(input())
nums = list(map(int,input().split()))
for i in nums[::-1]:
    if iseven(i):
        print(i)
        break