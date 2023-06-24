def isodd(n):
    if n%2==0:
        return False
    else:
        return True
s = int(input())
nums = list(map(int,input().split()))
for i in nums[::-1]:
    if isodd(i):
        print(i)
        break