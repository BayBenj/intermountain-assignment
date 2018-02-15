
for x in range(100):
	n = x + 1
	if n % 15 == 0:
		print("Fizz Buzz")
	elif n % 5 == 0:
		print("Buzz")
	elif n % 3 == 0:
		print("Fizz")
	else:
		print(n)
