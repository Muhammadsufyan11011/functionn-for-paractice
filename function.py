def greet(name):
	print ("assalam o alikim",name)
greet("khan")
def add(a,b):
	return a+b
print(add(2,4))
def even_check(number):
	if number % 2==0:
		return "SUFYAN IS GOOD"
	else:
		return "SUFYAN IS NOT GOOD"
print(even_check(4))
print(even_check(1))


def pehla_even_no(numbers):
	for num  in numbers:
		if num   % 2==0:
			return num
		
	return None
print(pehla_even_no([1,3,5,8]))

print(pehla_even_no([1,3,5]))