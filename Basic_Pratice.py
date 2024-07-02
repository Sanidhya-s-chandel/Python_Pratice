# 1) Accept numbers from a user

# x = int(input("Enter 1st number : "))
# y = int(input("Enter 2nd number : "))
# print(x,y)

# 2) Display three string “Name”, “Is”, “James” as “Name**Is**James”

# print("Name","Is","James",sep='**')

# 3) Display float number with 2 decimal places using print()

# x = round(76.855264216813 , 2)
# print(x)

# 4) Sum of two integers

# x = int(input("Enter 1st number : "))
# y = int(input("Enter 2nd number :"))

# print(x+y)

# 5) Accept two integers from user and print the sum
# 	Ex - The sum of 45 & 12 = 57

# x = int(input("Enter 1st number : "))
# y = int(input("Enter 2nd number :"))

# print(f"The sum of {x} and {y} is {x+y}")

# 6) Accept the User's name, age and print in following manner
# 	Ex - Hello Shery, you are 12 years old.

# name = input("Enter your name : ")
# age = input("Enter your age : ")

# print(f"Hello {name}, Your are {age} years old")

# 7) Accept the length and width of a rectangle. Calculate & print the area and perimiter

# length = float(input("Enter the length of  rectangle : "))
# width = float(input("Enter the width of the rectangle : "))

# perimeter = 2*(length + width)
# area = length*width

# print(f"The area of the rectangle is {area} and perimeter is {perimeter}")

# 8) Accept the marks of Robert in three subjects Maths, Computer, English respectively (each out of 100 ), 
#     Write a program to calculate his total marks and percentage marks.

# Maths = int(input("Enter the marks of Maths (out of 100) : "))
# Computer = int(input("Enter the marks of Computer (out of 100) : "))
# English = int(input("Enter the marks of English (out of 100) : "))

# total_marks = Maths + Computer + English
# percentage = total_marks/300 * 100

# print(f"the total marks of the student is {total_marks} with overall percentage is {percentage}")

# 9) Write a program to accept temperature in Fahrenheit & convert into Celsius. (Look for the formula on internet)

# fahren = int(input("Enter the temperature in *F : "))

# Celsius = (fahren - 32)*5/9

# print("The temperature in *C is",Celsius)

# 10) Accept the Principle amount, time & rate of interest and calculate the Simple Interest

# p = int(input("Enter the principle ammount : "))
# r = int(input("Enter the ROI : "))
# t = int(input("Enter the time period : "))

# SI = p*r*t/100

# print(f"The simple intrest of principle of rs {p} for time of {t} with rate of intrest {r} % is {SI}")

# 11) Take 3 int inputs from user and check and print the result.
# 	all are equal
# 	any of two are equal
# 	( use and or )

# x = int(input("Enter the number : "))
# y = int(input("Enter the number : "))
# z = int(input("Enter the number : "))

# if x == y and y == z:
#     print("All the numbers are equal :)")

# elif x == y or y == z or x == z:
#     print("Any two numbers are equal")

# elif x != y and x != z and y != z:
#     print("none of the numbers are equal")

# 12) Accept two numbers and print the greatest between them

# x = int(input("Enter the 1st number : "))
# y = int(input("Enter the 2nd number : "))

# if x > y:
#     print(x)

# elif x < y:
#     print(y)

# else:
#     print("Both the numbers are euqal !!")

# 13) Accept the gender from the user as char and print the respective greeting message
#      Ex - Good Morning Sir (on the basis of gender)

# gen = input("Enter the gender : ")

# if gen == 'm' or gen == 'M':
#     print("Good moring sir :)")

# else:
#     print("Good moring ma'am :)")

# 14) Extend the previous program and handle the wrong inputs.
#       Print Good Morning sir for input m or M & Good morning Maam for input F or f 
#       else print Wrong Input

# Gender = input("Enter your gender : ")

# if Gender == 'M' or Gender == 'm' or Gender == 'Male':
#     print("Good morning Sir :)")

# elif Gender == "F" or Gender == "f" or Gender == "Female":
#     print("Good morning ma'am :)")

# else:
#     print("Invalid Input !!")

# 16) Accept name and age from the user. Check if the user is a valid voter or not.
#       Vaid - Hello Shery, You are a valid voter.
#       Invalid - Sorry Shery, you can't cast the vote.
# 	Part 2 - Print after how many years the user will be eligible

# name = input("Enter your Name : ")
# age = int(input("Enter your age : "))

# if age >= 18:
#     print(f"Hello {name}, you are a vaild voter.. :)")

# elif age <= 18:
#     print(f"Sorry {name}, you can not vote")
#     print(18-age,"Years later you will be able to vote... :)")

# 17) Accept the parameters and calculate the Compound Interest & print it on STDOUT (Use Math class methods)

# p = int(input("Enter the principle amount : "))
# r = int(input("Enter the rate of intrest : "))
# t = int(input("Enter the time period : "))
# n = int(input("Enter the number of times intrest is applied : "))

# si = p*r*t/100
# ammount = si + p

# ci = p*(1+r/n)**n*t

# print(f"The compound intrest for principal : {p} rs is {ci}")

# 18) Accept a day number between 1-7 and print the corresponding dayname.

# day = int(input("Enter the number to find the day : "))

# if day == 1:
#     print("Its a Sunday...")

# elif day == 2:
#     print("Its a Monday...")

# elif day == 3:
#     print("Its a Tuesday...")

# elif day == 4:
#     print("Its a Wednesday...")

# elif day == 5:
#     print("Its a Thrusday...")

# elif day == 6:
#     print("Its a Friday...")

# elif day == 7:
#     print("Its a Saturday...")

# else:
#     print("Please Enter the vaild number to find the day...... !!")

# 19) Accept three numbers and print the greatest among them

# x = int(input("Enter the 1st number : "))
# y = int(input("Enter the 2nd number : "))
# z = int(input("Enter the 3rd number : "))

# if x > y and  x > z:
#     print(f"{x} is the greatest number")

# elif y > x  and y > z:
#     print(f"{y} is the greatest of them all")

# elif z > x and z > y:
#     print(f"{z} is the greatest number")

# elif x == y == z:
#     print("All the numbers are equal")

# elif x == y or x == z or y == z:
#     print("any two numbers are equal")

# 20) Accept a year and check if it a leap year or not (google to find out what's a leap year)

# year = int(input("Enter an year : "))

# if year % 4 == 0:
#     print("Its a leap year .... !!")

# elif year % 100 == 0 and year % 400 == 0:
#     print("its a leap year ... !!")

# elif year % 4 == 0 and year % 100 != 0:
#     print("its a leap year ...!!")

# else:
#     print("Its not a  leap year ... :)")

# 21) Write a program that will ask the user to enter his/her marks (out of 100). Define a method that will display grades according
#      to the marks entered as below:

#  	 Marks          Grade 
#  	 91-100          AA 
# 	 81-90           AB 
# 	 71-80           BB 
#    61-70           BC 
#    51-60           CD 
#    41-50           DD 
#  	 <=40            F

# marks = int(input("Enter the marks obtaines (out of 100) : "))

# if marks >= 91 and marks <= 100:
#     print("The grade alloted is AA")

# elif marks >= 81 and marks <= 90:
#     print("The grade alloted is AB")

# elif marks >= 71 and marks <= 80:
#     print("The grade alloted is BB")

# elif marks >= 61 and marks <= 70:
#     print("The grade alloted is BC")

# elif marks >= 51 and marks <= 60:
#     print("Yhe grade alloted is CD")

# elif  marks >= 41 and marks <= 50:
#     print("The grade alloted is DD") 

# elif marks <= 40:
#     print("Sorry you have failed .... !!! :(")

# else:
#     print("Please enter valid marks....!!!") 

# 22) Accept an english alphabet from user and check if it is a consonent or a vowel

# char = input("Enter the char to check : ")

# if char == "A" or char == "a":
#     print("Its a vowel :)")

# elif char == "E" or char == "e":
#     print("Its a vowel :)")

# elif char == "I" or char == "i":
#     print("Its a vowel :)")

# elif char == "O" or char == "o":
#     print("Its a vowel :)")

# elif char == "U" or char == "u":
#     print("Its a vowel :)")

# else:
#     print("Its constant... :)")

# 23) Accept two numbers from user and swap their values
#       Part 2 - Swap without using third variable

# x = int(input("Enter the value of x number : "))
# y = int(input("Enter the value of y number : "))

# z = x
# x = y
# y = z

# print(f"nummber after swaping are x : {x} and y : {y}")

# ------------------------------------------- OR (without using 3rd variable) -----------------------------------------------

# x = int(input("Enter the value of x number : "))
# y = int(input("Enter the value of y number : "))

# x = x + y
# y = x - y
# x = x - y

# print(f"The values of x and y after swaping are {x} and {y} respectively")

# x,y = y,x ---------------------------->>>> functionality used only in python


#               **ITERATIVE STATEMENTS**

# 24) Accept an integer and Print hello world n times

# x = int(input("Enter the number to print hello n times : "))

# for i in range(x):
#     print("Hello world.....!!!! :)")

# 25) Print natural number up to n

# x = int(input("Enter a number : "))

# for i in range(1,x+1):
#     print(i)

# 26) Reverse for loop. Print n to 1.

# x = int(input("Enter the number : "))

# for i in range(x,0,-1):
#     print(i)

# 27) Take a number as input and print its table
#        5 * 1 = 5
#        5 * 2 = 10 ... up to 10 terms

# x = int(input("Enter a number to print a table : "))

# for i in range(1,11):
#     print(f"{x} * {i} = {i*x}")

# 28) Sum up to n terms.

# x = int(input("Enter the number to print sum : "))
# sum = 0

# for i in range(1,x+1):
#     sum = sum + i

# print(f"The sum of first {x} naturals numbers is {sum}")

# 29) Factorial of a number

# x = int(input("Enter a number to find the factorial : "))
# fact = 1

# for i in range(1,x+1):
#     fact = fact * i

# print(f"The factorical of a number {x} is {fact}")

# 30) Print the sum of all even & odd numbers in a range seperately.

# x = int(input("Enter the number to set range : "))
# sum = 0
# sum2 = 0

# for i in range(x+1):
    
#     if i % 2 == 0:
#         sum += i
    
#     else:
#         sum2 += i

# print(f"The sum of even numbers is {sum} and odd numbers is {sum2}")

# 31) Print all the numbers which are either divisible by 3 or 5 in a range

# x = int(input("Enter a number to fix the range to print numbers divisible by  3 or 5 : "))

# for i in  range(1,x+1):
#     if i % 3 == 0 or i % 5 ==0:
#         print(i)

# 32) Print all the factors of a number.

# x = int(input("Enter a number to print its factors : "))

# for i in range(1,x+1):
#     if x % i == 0:
#         print(i)

# 33) Print the sum of all factors of a number, 50 - 1 + 2 + 5 + 10 + 25 = 43

# x = int(input("Enter the number to print the sum of all the factors : "))
# sum = 0

# for i in range(1,x):
#     if  x % i == 0:
#         sum += i

# print(sum)

# 34)  Accept a number and check if it a perfect number or not.
#       A number whose sum of factors(excluding number itself)  = Number 
#       Ex -  6 = 1, 2, 3 = 6

# x = int(input("Enter the number to check if its a perfect number or not : "))
# sum = 0

# for i in range(1,x):
#     if x % i == 0:
#         sum += i

# if sum == x:
#     print("Yess its a perfect number..... :)")

# else:
#     print("No its not a perfect number..... :(")

# 35) Seprate each digit of a number and print it on the new line

# x = int(input("Enter the number to print : "))

# while x > 0:
#     num = x % 10
#     print(num)
#     x //= 10

# 36) Sum of digits of a number, 936 = 18

# x = int(input("Enter a number : "))
# sum = 0

# while x > 0:
#     num = x % 10
#     sum += num
#     x //= 10

# print(sum)

# 37) Check if the number is Prime or not.

# x = int(input("Enter a number to check if it is a  prime or not : "))
# count = 0

# for i in range(1,x+1):
#     if x  % i == 0:
#         count += 1

# if count == 2:
#     print("Its a Prime number........:)")

# else:
#     print("Its a composite number......:(")

# 38) Accept a number and print its reverse

# x = int(input("Enter a number to print its reverse : "))
# num = 0

# while x > 0:
#     num = num * 10 + x % 10   # num*10 is used to fullfill the space(jo number me diff aayega 10s place ka woh remove ho jayega)
#     x //= 10

# print(f"The reverse of the given number is {num}")

# 39) Accept a number and check if it is a pallindromic number (If number and its reverse are equal)
#        Ex - 12321 - Rerverse - 12321

# x = int(input("Enter the number to check if it is pallindromic or not : "))
# copy = x
# num = 0

# while x > 0:
#     num = num * 10 + x % 10
#     x //= 10

# if num == copy:
#     print("Yess it's a pallindromic number :)")

# else:
#     print("No.... It's not a pallindromic number :(")

# 40) chech wether the number is a special number 	
#               153 = 1 + 125 + 27 = 153

# x = int(input("Enter a number to check if it is a special number : "))
# copy = x
# num = 0

# while x > 0:
#     z = x % 10
#     num += z**len(str(copy))
#     x //= 10

# if num == copy:
#     print("Yess It's a special number !!!!")

# else:
#     print("Noo Its not a special number !!!!")

# 41) Accept a number and check if it is a strong number or not (Sum of factorial of each digit)
#        Ex- 145 = 1! + 4! + 5! = 145

# x = int(input("Enter a number to check if its a strong number or not : "))
# copy = x
# sum = 0

# def factorial(a):
#     fact = 1
#     for i in range(1,a+1):
#             fact *= i
#     return fact

# while x > 0:
#       z = x % 10
#       sum += factorial(z)
#       x //= 10

# if sum == copy:
#       print("Yess It's a strong number......")

# else:
#       print("No.... It's not a strong number !!!!")

# =========================================  OR  =======================================================

# x = int(input("Enter the number to check if it is a strong number : "))
# copy = x
# sum = 0

# while x > 0:
#     z = x % 10
#     fact = 1

#     for i in range(1,z+1):
#         fact = fact*i
#     sum += fact
#     x //= 10

# if sum == copy:
#     print("Its a storng number......")

# else:
#     print("Its not a strong number !!!!")

# 42) Accept a number and check if it is a Harshad number 
#       Harshad number is a number or an integer which is completely divisible by sum of  its digits.
#       Ex - 24 = Sum of 2+4 = 6 & 24%6 = 0

# x = int(input("Enter a number to check if its a harshad number : "))
# copy = x
# sum = 0

# while x > 0:
#     z = x % 10
#     sum += z
#     x //= 10

# if copy % sum == 0:
#     print("Yes it is a harshad number...... :)")

# else:
#     print("Noo it is not a harshad number..... !!!!!")

# 43) Automorphic number 5 = 25 = 625 = 390625

# x = int(input("Enter a number to check if it is a automorphic number : "))
# y = x**2
# z = len(str(x))

# last = 0

# for i in range(z):
#     last = last * 10 + y % 10
#     y //= 10

# last = str(last)
# last = last[::-1]
# last = int(last)

# if last == x:
#     print("Its an automorphic number...... :)")

# else:
#     print("No its not an automorphiv number...... !!!!!!")

#                      **String Problems**

# 44) Compare two strings

# x = 'sanidhya'
# y = 'shanu'
# print(x==y)

# 45) Concatenate two strings

# x = 'sanidhya'
# y = 'singh'
# print(x+y)

# 46) Calculate Length of string

# x = "Sanidhya"
# # print(len(x))  #-------------------->>> only to be used in python 

# count = 0
# for i in x:
#     count += 1

# print(count)

# 47) Convert a string into upper case

# x = "sanidhya"
# print(x.upper())

# 48) Convert a string into lower case

# x = 'SANIDHYA'
# print(x.lower())

# 49) Copy a string from another string

# x = 'Sanidhya'
# y = ''

# for i in x:
#     y += i

# print(y)

# 50) Join two strings

# x = input("Enter a string to join : ")
# y = input("Enter another string to join : ")

# z = " ".join([x,y])
# print(z)

# 51) Arrange string characters such that lowercase letters should come first

# x = input("Enter a string : ")
# y = ""
# z = ""

# for i in x:
#     if i.islower():
#         y += i

#     if i.isupper():
#         z +=i

# print(y+z)

# 52) Count all letters, digits, and special symbols from a given string
#     Given: str1 = "P@#yn26at^&i5ve"
#     Expected Outcome:
    # Total counts of chars, digits, and symbols
    # Chars = 8
    # Digits = 3
    # Symbol = 4

# x = input("Enter a string : ")
# char = 0
# digits = 0
# symbol = 0

# for i in x:
#     if i.isalpha():
#         char += 1
    
#     elif i.isnumeric():
#         digits += 1

#     else:
#         symbol += 1

# print(f"""Total counts of chars, digits, and symbols :
#     Chars = {char}
#     Digits = {digits}
#     Symbols = {symbol} """)

# 53) Print string in reverse,its length,in uppercase,lowercase and copy into another string

# x = input("Enter a string : ") 
# y = ""
# z = ""

# # print(x[::-1]) ------------->>> to print in reverse using functions

# for i in x:
#     y = i + y
#     z += i              #--------------->>> copy sting to z

# print("The reverse for the string is :",y)
# print("lenght of stirng is :",len(x))
# print("The upper for the stirng is:",x.upper())
# print("The lower for the stirng is:",x.lower())
# print("The copyed string is:",z)

# 54) Count alphabets, digits and symbols from a given string

# x = input("Enter a string : ")
# char = 0
# digits = 0
# symbol = 0

# for i in x:
#     if i.isalpha():
#         char += 1
    
#     elif i.isnumeric():
#         digits += 1

#     else:
#         symbol += 1

# print(f"""Total counts of chars, digits, and symbols :
#     Chars = {char}
#     Digits = {digits}
#     Symbols = {symbol} """)

# 55) Compare two strings without using inbuilt functionsx

# x = input("Enter a string : ")
# y = input("Enter another string : ")

# def check(a,b):
#     equal = True
    
#     if len(a) != len(b):
#         equal = False
#         print("strings are not equal...... !!!")

#     else:
#         for i in range(len(a)):
#             if a[i] != b[i]:
#                 equal = False
#                 print("Strings are not equal.... !!!!!")
#                 break

#     if equal:
#         print("Yess the strings are equal...... !!!!")

# check(x,y)

# 56) Count Vowels from given string

# x = input("Enter a string to check the vowel : ")

# def count(a):
#     count = 0
#     for i in a:
#         if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#             count += 1
        
#         elif i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
#             count += 1
    
#     print("The numbers of vowels in the given string is",count)

# count(x)

# 57) Reverse a string

# x = input("Enter a string : ")
# y = ""

# for i in x:
#     y = i + y

# print("The reverse of the string is :",y)

# 58) Check string is Pallindrome or not**

# x = input("Enter a string to check if it is pallindromic : ")
# copy = x
# y = ""

# for i in x:
#     y = i + y

# if y == copy:
#     print("Its a pallindromic string......... :)")

# else:
#     print("Noo.... Its not a pallindromic string !!!!")

#                     **01 LIST PROBLEMS**

# 59) Accept List elements and reprint it

# x = input("Enter the elements in the list : ")
# l = []

## l = x.split()   #------------------------>>> this is used to enter the string in form of list and can also sep items on basis
                   #                              of enterd chr or value (mainly used for strings)

# l.append(x)
# print(l)         #------------------------>>> this is used to append single element in the list

# x = int(input("Enter the no. of elements in the list : "))
# l = []

# for i in range(x):
#     y = input("Enter the elements in the list : ")
#     l.append(y)

# print("The entered list is :",l)

# 60) Print  List elements in reverse order

# x = int(input("Enter the no. of elements in the list : "))
# l = []

# for i in range(x):
#     y = input("Enter the element in the list : ")
#     l.append(y)

# print(l[::-1])              #---------------->>> reverse through indexing in python
# print(list(reversed(l)))    #================>>> used only in python(reversed()) fun. but need to convert into the req. category

# 61) Print Fibonacci series using List

# x = int(input("Enter a number : "))
# l = [0,1]
# a = l[0]
# b = l[1]
# c = 0

# for i in range(x):
#     c = a + b
#     a = b
#     b = c
#     l.append(c)

# print(l)

# 62) Print positive and negative elements of an List

# x = int(input("Enter the no. of elements in a list : "))
# l = []
# l2 = []
# l3 = []

# for i in range(x):
#     y = int(input("Enter the element : "))
#     l.append(y)

# for i in l:
#     if i >= 0:
#         l2.append(i)

# for i in l:
#     if i < 0:
#         l3.append(i)
    
# print("The positive elements in the list are :",l2)
# print("The negative elements in the list are :",l3)

# 63) Print list in ascending or descending order

# x = input("Enter the elements in the list : ").split()
# x.sort()                      #------------------------------------>>>> using inbuild function to sort in accending
# print(x)

# x = input("Enter the element of the list : ").split()
# x.sort(reverse = True)        #------------------------>>> can be used to print in descending but all chr. are treated as  
# print(x)                      #    string so double digit input gives worng output convert elements into int() for corretness.

# x = input("Enter the elements : ").split()
# x = [int(i) for i in x]
# x.sort(reverse=True)
# print(x)

# 64) Accept size n from user and create a n size List then take n inputs into the and finally 
#    Print the sum of all elements in the List in the following manner
#    10 + 20 + 30 = 60

# x = int(input("Enter the number of elements int he list : "))
# l = []
# sum = 0

# for i in range(x):
#     z = int(input(f"Enter the elements in the list : "))
#     l.append(z)

# for i in l:
#     sum += i

# print(" + ".join(map(str,l)),f"= {sum}")

# 65) Mean of List elements.

# x = int(input("Enter the number of elements in the list : "))
# l = []
# sum = 0

# for i in range(x):
#     y = int(input(f"Enter the {i+1} element : "))
#     l.append(y)

# for j in l:
#     sum += j

# mean = sum/len(l)
# print(f"The mean of the elements of the list is {mean}")

# 66) Find the greatest element and print its index too.
#    {2, 96, 69, 77, 145, 20} = Max element = 145 found at 4 index

# x = int(input("Enter the number of elements in the list : "))
# l = []
# maxx = 0
# index = 0

# for i in range(x):
#     y = int(input(f"Enter the {i+1} element : "))
#     l.append(y)

# for i in range(len(l)):
#     if l[i] > maxx:
#         maxx = l[i]
#         index = i

# print(f"The greatest element in the list is {maxx} at index point {index}")

# 67) Find the smallest element and print its index too.
#    {2, 96, 69, 77, 145, 20} = Min element = 2 found at 0 index

# x = int(input("Enter the number of elements : "))
# l = []

# for i in range(x):
#     y = int(input(f"Enter the {i+1} element : "))
#     l.append(y)

# minn = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] < minn:
#         minn = l[i]
#         index = i

# print(f"The smallest element in the list is {minn} at index point {index}")

# 68) Find the second greatest element 
#    {2, 96, 69, 77, 145, 20} = Second greatest element = 96

# x = int(input("Enter the number of elements in the list : "))
# l = []
# maxx = 0
# maxx2 = 0
# index = 0 
# index2 = 0

# for i in range(x):
#     z = int(input(f"Enter the {i+1} element of the list : "))
#     l.append(z)

# for i in range(len(l)):
#     if l[i] > maxx:
#         maxx2 = maxx
#         maxx = l[i]
#         index2 = index
#         index = i
    
#     elif l[i] > maxx2 and l[i] < maxx:
#         maxx2 = l[i]
#         index2 = i

# print(f"The greatest element of the list is {maxx} at index print : {index}")
# print(f"The secound greates element of the list is {maxx2} at index point : {index2}")

# 69) Check if List is sorted or not.

# x = int(input("Enter the number of elements in the list : "))
# l = []
# flag = True

# for i in range(x):
#     z = int(input(f"Enter the {i+1} element : "))
#     l.append(z)

# # l.sort()          #------------------------>>>> sort() fun used to sort the list (just for testing of the code it is used here)
# print(l)

# for i in range(len(l)-1):
#     if l[i] <= l[i+1]:
#         continue

#     else:
#         flag = False
#         print("Your List is unsorted..... :(")
#         break

# if flag == True:
#     print("Your list is sorted.... :)")

# 70) Pallindromic List - Write a program to check. 
#     if elements of an List are same or not it read from front or bacExample : arr= [2,3,15,15,3,2]

# x = int(input("Enter the number of elements : "))
# l = []
# l2 = []

# for i in range(x):
#     z = int(input(f"Enter the {i+1} element : "))
#     l.append(z)              #---------------------->>>> this code takes more space and time complexity so we can use 
#                              #---------------------->>>> 2-pointer method to reduce space and time complexity respectively

# for i in range(len(l)):
#     l2.append(l[i])

# if l == l2[::-1]:
#     print("The entered list is pallindromic.........")

# else:
#     print("The entered list is not pallindromic........")

# ================================>>>> 2 - POINTER METHOD <<<<=========================================

# x = int(input("Enter the number of elements in the list : "))
# l = []
# flag = True

# for i in range(x):
#     z = int(input(f"Enter the {i+1} element : "))
#     l.append(z)

# i = 0
# j = len(l)-1                   #-------------------->>>> 2-pointer method for a list using while loop

# while i < j:                   #====================>>> Have less space and and time complexity
#     if l[i] != l[j]:
#         print("The list is not pallaindromic...... :(")
#         flag = False
#         break

#     i += 1
#     j -= 1

# if flag:
#     print("The list is pallindromic...... :)")

# ------------------------------------>>>> FoR loop <<<<---------------------------------------------

# x = int(input("Enter the number of elements in the list : "))
# l = []
# flag = True

# for i in range(x):
#     z = int(input(f"Enter the {i+1} element : "))
#     l.append(z)

# i = 0
# j = len(l)-1

# for i in range(len(l)//2):          #--------------------->>> makes loop ittrates only half of the loop
#     if l[i] != l[j]:
#         print("The Given list is not pallindromic..... :(")
#         flag = False
#         break

#     i += 1
#     j -= 1 

# if flag:
#     print("The given list is pallindromic........ :)")

# 71) List left Rotation by 1

# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# n = 1

# for i in range(n):
#     temp = l[0]
    
#     for j in range(len(l)-1):
#         l[j] = l[j+1]

#     l[len(l)-1] = temp

# print(l)

# 72) List right Rotation by 1

# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# n = 1

# for i in range(n):
#     temp = l[len(l)-1]

#     for j in range(len(l)-1,-1,-1):
#         l[j] = l[j-1]
    
#     l[0] = temp

# print(l)

# 73) List left rotation by K elements

# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# x = int(input("Enter the number of elements to rotate the list : "))

# for i in range(x):
#     flag = l[0]

#     for s in range(len(l)-1):
#         l[s] = l[s+1]

#     l[len(l)-1] = flag

# print(l)

# 74) List right rotation by K elements

# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# x = int(input("Enter a number to rotate the list : "))

# for i in range(x):
#     flag = l[len(l)-1]

#     for s in range(len(l)-1,-1,-1):
#         l[s] = l[s-1]

#     l[0] = flag

# print(l)

# 75) List Reverse Using Extra space
# using extra space means that we can use another list that is empty as we have done previously

# l = [1,2,3,4,5,6,7]
# l2 = []

# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])

# print(l2)

# 76) List Reverse Without Using Extra space
# without using extra space means we can't store data in another list or empty variable

# l = [1,2,3,4,5,6,7,8,9,10]

# i = 0
# end = len(l)-1

# for i in range(len(l)//2):
#     l[i],l[len(l)-i-1] = l[len(l)-i-1],l[i]

#     i += 1
#     end -= 1

# print(l)

#----------------------------------->>>> using while loop <<<<---------------------------------------------

# l = [1,2,3,4,5,6,7,8,9,10]

# i = 0
# s = len(l)-1

# while i < s:
#     l[i],l[len(l)-i-1] = l[len(l)-i-1],l[i]

#     i += 1
#     s -= 1

# print(l)

# 77) Linear Search an List - If element found print the index else -1

# l = [43, 12, 76, 32, 90, 54, 23, 67, 89, 14, 31, 78, 45, 9, 61]

# x = int(input("Enter the element of the list u want to find : "))
# flag = False

# for i in range(len(l)):
#     if l[i] == x:
#         flag = True
#         break

#     else:
#         flag = False

# if flag == True:
#     print(f"The element {x} was found at index : {i}")

# else:
#     print(-1)

# 78) Binary Search. If element found print the index else -1

# l = [43, 12, 76, 32, 90, 54, 23, 67, 89, 14, 31, 78, 45, 9, 61]

# x = int(input("Enter the element to find : "))
# i = 0
# s = len(l)-1
# flag = False

# while i < s:  # using 2 - pointer technique
#     if l[i] == x or l[s] == x:
#         flag = True
#         break

#     else:         # this is a two pointer method so can be applied when the list is not sorted and is not pure binary search
#         flag = False

#     i += 1
#     s -= 1

# if flag:
#     print(f"The element {x} was found at index : {i}")
# else:
#     print(-1)

# -------------------------------------->>>> Binary Search <<<<---------------------------------------------------

# l = [43, 12, 76, 32, 90, 54, 23, 67, 89, 14, 31, 78, 45, 9, 61]
# x = int(input("Enter the number to search : "))
# l.sort()

# first = 0
# last = len(l)-1

# print(f"The sorted list is {l}")

# while first <= last:
#     mid = ((first+last)//2)
#     if l[mid] == x:
#         print(f"The number {x} was found at index {mid}")
#         break
    
#     elif l[mid] > x:
#         last = mid - 1

#     else:
#         first = mid + 1

# if first > last:
#     print("Entered number is not found in the list : (-1)")

# 79) Move all the negative elements on left side and positive elements on right side with extra space in O(n).

# l = [43, -12,-76, 32, -90, 54,-23, 67, 89, -14, 31, -78, 45,- 9, 61]
# l2 = []
# l3 = []

# for i in range(len(l)):
#     if l[i] < 0:
#         l2.append(l[i])

#     else:
#         l3.append(l[i])

# print(l2+l3)

# 80) Move all the negative elements on left side and positive elements on right side without extra space in O(n).

# l = [43, -12,-76, 32, -90, 54,-23, 67, 89, -14, 31, -78, 45,- 9, 61]

# i = 0
# s = len(l)-1

# while i <= s:
        
#     if l[i] < 0:
#         i += 1

#     elif l[s] >= 0:
#         s -= 1

#     else:
#         l[i],l[s] = l[s],l[i]
#         i += 1
#         s -= 1 

# print(l)

# 81) Bubble Sort.

# l = [43, 12, 76, 32, 90, 54, 23, 67, 89, 14, 31, 78, 45, 9, 61]

# for i in range(len(l)):
#     for s in range(len(l)-1):
#         if l[s] > l[s+1]:
#             l[s],l[s+1] = l[s+1],l[s]

# print(l)

# 82) Median of List elements

# l = [43, 12, 76, 32, 90, 54, 23, 67, 89, 14, 31, 78, 45, 9, 61,33]
# l.sort()
# n = len(l)

# if len(l) % 2 != 0:
#     median = (n-1)//2
#     mid = l[median]
    
# else:
#     median = n//2
#     median2 = median - 1
#     mid = (l[median] + l[median2])/2

# print("The median of the given list is",mid)

# 83) Strong number using methods

# x = int(input("Enter a number to check if its a strong number or not : "))
# copy = x
# sum = 0

# def factorial(a):
#     fact = 1
#     for i in range(1,a+1):
#             fact *= i
#     return fact

# while x > 0:
#       z = x % 10
#       sum += factorial(z)
#       x //= 10

# if sum == copy:
#       print("Yess It's a strong number......")

# else:
#       print("No.... It's not a strong number !!!!")

# 84) Number of even and odd elements in an List

# l = [43, 12, 76, 32, 90, 54, 23, 67, 89, 14, 31, 78, 45, 9, 61,33]

# count = 0
# count2 = 0

# for i in l:
#     if i % 2 == 0:
#         count += 1
#     else:
#         count2 += 1
    
# print(f"The number of even elements in the list are {count} and number of odd elements are {count2}")

# 85) Sum of all odd frequency elements in an List

# x = int(input("Enter the number of elements in the list : "))
# l = []

# for i in range(x):
#     n = int(input(f"Enter the {i+1} element of the list : "))
#     l.append(n)

# sum = 0

# for i in range(len(l)):
#     if l[i] % 2 != 0:
#         sum += l[i]

# print(f"The sum of all odd frequency in the list is {sum}")



#                       **Dictionary (hash map) questions**

# 86) Write a Python program to iterate over dictionaries using for loops

# dict = {"Name" : "Sanidhya", 'Age' : 20, "Gender" : "Male"}

# for i in dict:
#     print(f"{i} : {dict[i]}")

# ---------------------------->>>>> OR we can use .items() <<<<<------------------------------------------------

# dict = {"Name" : "Sanidhya", 'Age' : 20, "Gender" : "Male"}

# for i,s in dict.items():
#     print(f"{i} : {s}")          # The items() method of a dictionary returns a view of its key-value pairs.

# 87) Write a Python script to merge two Python dictionaries.

# dict = {"Name" : "Sanidhya", "Age" : 20}
# dict2 = {"Gender" : "Male", "Study" : "B.tech"}    # **variable_of_dictonary this is used to unpack the dictionary

# dict3 = {**dict,**dict2}
# print(dict3)

# ---------------------------------->>>>> Method 2 (loop) <<<<<---------------------------------------------------

# dict = {"Name" : "Sanidhya", "Age" : 20}
# dict2 = {"Gender" : "Male", "Study" : "B.tech"}

# dict3 = dict.copy()

# for  i, s in dict2.items():           .items() ---->> This method returns a view of the key-value pairs (items) as tuples.
#     dict3[i] = s

# print(dict3)

#------------------------------->>>>> Method 3 (update) <<<<<-----------------------------------------------------

# dict = {"Name" : "Sanidhya", "Age" : 20}
# dict2 = {"Gender" : "Male", "Study" : "B.tech"}

# dict3 = dict.copy()
# dict3.update(dict2)

# print(dict3)

# -------------------------------->>>>> Method 4 ( | operator ) <<<<<---------------------------------------------

# dict = {"Name" : "Sanidhya", "Age" : 20}
# dict2 = {"Gender" : "Male", "Study" : "B.tech"}

# print(dict | dict2)  # | is a union operator used to provide uninon if the dictionary or the set

# 88) Write a Python program to sum all the values in a dictionary

# dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}       # Add the key-value pair to the dictionary using ( my_dict[key] = value)

# sum = 0

# for i in dict:
#     sum += dict[i]

# print("The sum of all the values in the dictionaty is",sum)

# 89) Convert a list to dictionary 

# ============================================>>>> using two list <<<<===============================================

# l = ["a","b","c","d","e"]               # KEYS
# l2 = [1,2,3,4,5]                        # VALUES OF THE KEYS

# d = dict(zip(l,l2))      # zip is used to pack values in tuples of the list
# print(d)

# ---------------------------------------->>>> using a single list <<<<-------------------------------------------------

# l = [1, 'one', 2, 'two', 3, 'three']
# dict = {}

# for i in range(0,len(l),2):
#     values = l[i]
#     keys = l[i+1]

#     dict[keys] = values

# print(dict)

# 90) count the frequency of each elements

# dict = {'apple': 2, 'banana': 3, 'orange': 2, 'grape': 1, 'kiwi': 3}
# dict2 = {}

# for i in dict.values():             # .values() is used to get the values of the key
#     if i in dict2:
#         dict2[i] += 1 
    
#     else:
#         dict2[i] = 1

# print(dict2)

# 91) Write a Python program to combine two dictionary by adding values for common keys.

# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 5, 'c': 15, 'd': 25}

# dict3 = {}

# dict3 = dict1.copy()

# for i,s in dict2.items():
#     if i in dict3:
#         dict3[i] += s

#     else:
#         dict3[i] = s

# print(dict3)

# 92) replace the maximum appearing number in a list with 0

# dict = {'a': 5, 'b': 8, 'c': 5, 'd': 3, 'e': 8, 'f': 3, 'g': 5}
# dict2 = {}

# for i in dict.values():
#     if i in dict2:
#         dict2[i] += 1

#     else:
#         dict2[i] = 1

# max_appearing_value = max(dict2, key = dict2.get) # this line gives the maximum occuring key .get() is used to get value of the key

# for i,s in dict.items():
#     if dict[i] == max_appearing_value:
#         dict[i] = 0

# print(dict)

#                                      **Patterns questions**


# 93) Right Triangle - Star

#       	*
#       	* *
# 	        * * *
#       	* * * *
#       	* * * * *

# x = int(input("Enter the number of rows in the pattern : "))

# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print("*",end="")
    
#     print(" ")

# 94) Right Triangle - Number

#    	1                            #   1
# 	    1 2                          #   22
# 	    1 2 3                OR      #   333
#   	1 2 3 4                      #   4444          
#   	1 2 3 4 5                    #   55555

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(1,x+1):
#     for j in range(1,i+1):          # 2nd loop me j lene pe 1st wala pattern aata h and i lene pe 2nd wala
#         print(j,end='')
    
#     print("")

# #------------------------------------------>>>>>  OR  <<<<<--------------------------------------------------
    
# x = int(input("Enter the number of rows t0 print the pattern : "))

# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print(i,end="")

#     print("")

# 95) Right Triangle - Alphabet

#        	A                               # A
# 	        A B                             # BB
# 	        A B C            OR             # CCC
# 	        A B C D                         # DDDD
# 	        A B C D E                       # EEEEE

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(65,x+65):         # use ascii values for the alphabets and then convert them into the char form
#     for j in range(65,i+1):      # ascii values of A is 65
#         print(chr(j),end="")        
    
#     print("")

# # ================================>>>>> OR <<<<<==========================================

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(65,x+65):
#     for j in range(65,i+1):
#         print(chr(i),end="")

#     print("")

# 96) Inverted Right Triangle

#    	* * * * *
#   	* * * *
#   	* * *
#   	* *
# 	    *

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(x-1,-1,-1):
#     for j in range(i,-1,-1):
#         print("*",end="")
#     print("")

# 97) Mirrored Right Triangle

# 	            *
# 	          * *
# 	        * * *
# 	      * * * *
#   	* * * * *

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(x):

#     for j in range(x-i-1):
#         print(" ",end="")

#     for j in range(i+1):
#         print("*",end="")

#     print()

# =================================>>>>> using single for loop <<<<<=============================================

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(x):
#     print(" "*(x-i-1) + "*"*(i+1))  # this is string multiplication method


# 98) Mirrored Inverted Right Triangle

#      	* * * * *
#   	  * * * *
# 	        * * *
# 	          * *
# 	            *

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(x+1):
#     print(" "*(i+1) + "*"*(x-i))

# ------------------------------------------------>>>> OR <<<<----------------------------------------------------

# x = int(input("Enter the number of rows to print the pattern : "))
# k = 0
# z = x

# for i in range(1,x+1):
        
#     print(" "*k,"*"*z,end="")
#     k += 1
#     z -= 1 
#     print()

# 99) Triangle

# 	    *                                *
# 	   * *                              ***
# 	  * * *             OR             *****
# 	 * * * *                          *******      (2nd pattern) 
# 	* * * * *	                     *********

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(x):
    
#     for j in range(x-i-1):
#         print(" ",end="")
    
#     for j in range(i+1):        # use range(2*i+1) and no space in end="" to print the 2nd patterm
#         print("*",end=" ")
    
#     print("")

# -------------------------------------->>> OR <<<---------------------------------------------


# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(x):
    
#     for j in range(x-i-1):
#         print(" ",end="")
    
#     for j in range(2*i+1):        # like this
#         print("*",end="")
    
#     print("")

# 100) Inverted Triangle

#      	* * * * *
#    	 * * * *
#   	  * * *
#   	   * *
#   	    *

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(x):
    
#     for j in range(i):
#         print(" ",end="")

#     for j in range(x-i):          # 2*(x-i)-1 for the 2nd inverted pattern (jo upar 2nd wala h uska inverted triangle)
#         print("*",end=" ")        # isme end="" ka space hata dena h

#     print("")

# 101) Diamond or Kite

# 	     *      
# 	    * *     
# 	   * * *    
# 	  * * * *   
# 	 * * * * *  
# 	* * * * * * 
# 	 * * * * *  
# 	  * * * *   
# 	   * * *    
# 	    * *     
# 	     *   

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(0,x):
    
#     for j in range(0, x-i-1):
#         print(" ",end="")

#     for j in range(0,i+1):
#         print("*",end=" ")
    
#     print("")

# for i in range(0, x-1):

#     for j in range(0,i+1):
#         print(" ",end="")

#     for j in range(0, x-i-1):
#         print("*",end=" ")    
    
#     print("")


#                               **FILES AND OOPS** (This can change from BATCH to BATCH)

# 102) Program to create Employee, store values and reprint

class Employee:
    def __init__(self,name,salary,occupation):
        self.name = name
        self.salary = salary
        self.occupation = occupation

    def  show(self):
        print(f"The name is : {self.name} with salary : {self.salary} and is a {self.occupation}")

name = input("Enter the name : ")
salary = int(input("Enter the salary : "))
occupation = input("Enter the occupation : ")

x = Employee(name,salary,occupation)
print(x.show())

# 103) Program to read and write contents to a file character by character