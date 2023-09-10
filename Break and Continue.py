s = 'Mahesh'
for letter in s:
print(letter)
	if letter == 'e' or letter == 's':
		break
print("Out of for loop")
print()

i = 0
while True:
	print(s[i])
	if s[i] == 'e' or s[i] == 's':
		break
	i += 1

print("Out of while loop")
