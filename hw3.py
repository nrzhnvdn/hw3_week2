#1
# a = int(input("First number\n"))
# operand = input("What do you want\n")
# b = int(input("Second number\n"))

# if operand == '+':
# 	res = (a+b)
# elif operand == '-':
# 	res = (a-b)
# elif operand == '/':
# 	res = (a/b)
# elif operand == '*':
# 	res = (a*b)
# elif operand == '**':
# 	res = (a**b)
# elif operand == '%':
# 	res = (a%b)
# elif operand == '//':
# 	res = (a//b)
# else:
# 	print ('the result is invalid')
# print (f'answer is: {res}')

#2
# a = int(input("First number\n"))
# b = int(input("Second number\n"))
# if a%b == 0:
# 	print ("divides")
# else:
# 	print ("does not divide")

#3
# a = input("Password\n")
# b = input("Repeat Password\n")
# if a==b:
# 	print ("password is correct")
# else: 
# 	print ("password is not correct")

#4
# n = int(input("Number of students "))
# k = int(input("Number of apples "))
# print(k//n)
# print(k%n)

#5
# n = int(input("Zoom "))
# k = int(input("Flash "))
# if n<k:
# 	print ("YES")
# if n>k:
# 	print ("NO")
# else:
# 	print ("Don't know")

#6
# largest = None
# smallest = None
# list1 = []
# while True:
#     num = input("Enter a number: ")
#     if num == "done" : break
#     try:
#         val = int(num)
#         if int(num):
#             list1.append(num)
#     except:
#         print("Invalid input") 
# print("Maximum is " + max(list1))
# print("Minimum is " + min(list1))

#7
# n = int(input("Number of kg "))
# if 0<n<60:
# 	print ("a light weight")
# if 60<n<64:
# 	print ("first welterweight")
# if 64<n<69:
# 	print ("welterweight")
# else:
# 	print ("fatty")

#8
# n = input("Gender ")
# k = int(input("Age "))
# if n=='m' and k>20:
# 	print ("Welcome")
# if n=='f' and k>17:
# 	print ("Welcome")
# else:
# 	print ("No entry")

#9
# n = input("Enter a three-digit number: ")
# n = int(n)
 
# d1 = n % 10
# d2 = n % 100 // 10
# d3 = n // 100

# print("Sum of +:", d1 + d2 + d3)
# print("Sum of *:", d1 * d2 * d3)

#10
sq = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
bq = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 31, 33, 35)
a = int(input())
if a == sq:
print('red')
elif a == bq:
print('black')
elif a == 0:
print('green')
else:
print('error')