# def myfunc():
# 	print("Hello python Lovers")
# myfunc()

# def detailes(name,userId,country):
# 	print("Name:-",name)
# 	print("UserId:-",userId)
# 	print("Cuntry:-",country)
# detailes("SUFYAN","SUFYAN##1232","PAKISTAN")

# def greet(name):
# 	print ("assalam o alikim",name)
# greet("khan")
# def add(a,b):
# 	return a+b
# print(add(2,4))
# def even_check(number):
# 	if number % 2==0:
# 		return "SUFYAN IS GOOD"
# 	else:
# 		return "SUFYAN IS NOT GOOD"
# print(even_check(4))
# print(even_check(1))


# def pehla_even_no(numbers):
# 	for num  in numbers:
# 		if num   % 2==0:
# 			return num
		
# 	return None
# print(pehla_even_no([1,3,5,8]))

# print(pehla_even_no([1,3,5]))


# def squre(num):
# 	if num %2==0:
# 		print("Even number")
# 	else:
# 		print("Odd number")
# squre(4)
# squre(3)

# def square(n):
# 	n=n*n 
# 	return n 
# print(square(10))
# """enven and odd test"""
# def  even_odd(num):
# 	if num % 2==0:
# 		print(num,"is even number")
# 	else:
# 		print(num,"is odd number")
# print(even_odd(3))
# print(even_odd(4))


# """concatenate string"""
# def fulname(firstname,midlename,lastname):
# 	fulname="{} {} {}".format(firstname,midlename,lastname)
# 	print(fulname)
# print(fulname("ali","hamza","khan"))

# def fulname(firstname,lastname,midlenmae):
# 	fulname="{},{},{}".format(firstname,midlenmae,lastname)
# 	print(fulname)

# print(fulname(lastname="ali" ,midlenmae="khan" ,firstname="usman"))
 





# def add_numbers(a,b):
#  	result=a+b 
#  	return result
# sum=add_numbers(5,3)
# print("sum is :",sum)


# def my_name(firstname):

# 	print("Mera name sufyan hy or :",firstname)

# my_name("ali")


# def greet_user(name):
# 	print("Assalam o alikum,",name)
# user_name=input("Apna name lekho:")
# greet_user("Ahmad")

# def calculator(a,b,operation):
# 	if operation == "add":
# 		return a + b
# 	elif operation == "subtract":
# 		return a - b
# 	elif operation == "multiply":
# 		return a * b 
# 	elif operation == "divide":
# 		if b != 0:
# 			return a/b
# 		else:
# 			return "Division by zero is not allowed "
# 	else:
# 		return "Invalid operation"
# num1=10
# num2=5
# result= calculator(num1,num2,"add")
# print("Result:",result)
# print(calculator(12,4,"subtract"))
# print(calculator(6,3,"multiply"))
# print(calculator(8,2,("divide")))




balance=10000
def atm_withdraw(amount):
	global balance
	if amount > balance:
		print("Sufficient balance")
	else:
		balance -= amount
		print("withdraw is successful")
		print("Remaining balance:",balance)
atm_withdraw(3000)
atm_withdraw(8000)

def atm():
	balance = 5000
	amount = int(input("kitna passa nekalna chaty ho"))
	if amount > balance:
		print("balance kam hy")
	else:
		balance -= amount
		print("withdraw successful")
		print("New balance:",balance)
atm()