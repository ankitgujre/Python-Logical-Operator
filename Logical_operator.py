

print(0 and 1)
print(20 and 100)
print(0 or 1)
print(not 0)

# check the greatest between three number

# num1 = int(input("Enter 1st number :"))
# num2 = int(input("Enter 2nd number :"))
# num3 = int(input("Enter 3rd number :"))

# if num1 > num2 and num1 > num3:
#     print("greatest = ", num1)
# elif num2 > num1 and num2 > num3:
#     print("greatest = ", num2)
# elif num3 > num1 and num3 > num2:
#     print("greatest = ", num3)
# else:
#     print("Invalid entry")


# check the email and password is correct or not

# email = input("Enter your email: ")
# pwd = int(input("Enter your password : "))

# if email == "admin@gmail.com" and pwd == 1234567890:
#     print("login")
# else:
#     print("invalid")
    
    
# check the number is divisible by 2 and 4

# num = int(input("Enter digit: "))

# if num % 2 == 0 and num % 4 == 0:
#     print("completely divisible by 2 and 4")
# else:
#     print("not divisible")

# check the number is inbetween 0-50

# num = int(input("Enter number: "))

# if num > 0  and num <=50:
#     print("Yes")
# else:
#     print("no")

# check the number above 50 and divisible by 4?

num = int(input("Enter number: "))

if num > 50 and num % 4 == 0:
    print("greater than 50 and divisible by 4")
elif num > 50 and num % 4 != 0:
    print("greater than 50 but not divisible by 4")
else:
    print("not greater than 50")
    
# check vowel and consonant

alpha = input("Enter alphabet ")
if alpha == "a" or alpha == 'e' or alpha =='i' or alpha == 'u':
    print("vowel ", alpha)
else:
    print("Consonant", alpha)