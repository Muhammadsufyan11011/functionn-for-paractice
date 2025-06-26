def myfunc():
	print("Hello python Lovers")
myfunc()

def detailes(name,userId,country):
	print("Name:-",name)
	print("UserId:-",userId)
	print("Cuntry:-",country)
detailes("SUFYAN","SUFYAN##1232","PAKISTAN")

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


def squre(num):
	if num %2==0:
		print("Even number")
	else:
		print("Odd number")
squre(4)
squre(3)

def square(n):
	n=n*n 
	return n 
print(square(10))
"""enven and odd test"""
def  even_odd(num):
	if num % 2==0:
		print(num,"is even number")
	else:
		print(num,"is odd number")
print(even_odd(3))
print(even_odd(4))


"""concatenate string"""
def fulname(firstname,midlename,lastname):
	fulname="{} {} {}".format(firstname,midlename,lastname)
	print(fulname)
print(fulname("ali","hamza","khan"))

def fulname(firstname,lastname,midlenmae):
	fulname="{},{},{}".format(firstname,midlenmae,lastname)
	print(fulname)

print(fulname(lastname="ali" ,midlenmae="khan" ,firstname="usman"))
 


