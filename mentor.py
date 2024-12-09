# Question 1
# a = int(input("enter the no"))
# copy = a
# reverse = 0                                
# while a !=0:                      
#     reverse = reverse*10 + a%10
#     a = a//10
# if reverse == copy:
#     print(" It is a palidromic number")
# else:
#     print(" It is not a palindromic number")

# Question 2
# m = int(input("enter the no"))
# copy = m
# summ = 0
# while m != 0 :
#     a = m%10
#     fact = 1
#     for i in range(1,a+1):       
#         fact = fact*i
#     summ = summ +fact
#     m = m//10
# print(summ)
# if summ == copy:
#     print("strong no ")
# else:
#     print("the no is not stronf no")

# Question 3 
# a = int(input("enter the no"))
# copy = a 
# summ = 0
# while a != 0:
#     summ = summ + a%10             
#     a = a//10
# if copy % summ == 0:
#     print(" It is harshadd no")
# else:
#     print(" It is not a harshad no")

# Question 4
# a = int(input("enter the no"))
# copy = a
# summ = 0                             
# while a != 0:
#     summ = summ + a**len(str(copy))
#     a = a //10
# if summ == copy:
#     print(" It is special no")
# else :
#     print(" It is not special ")

#accept element in list and tell an element occured how many times
# l = []
# a = int(input("enter the no"))    
# for i in range(a):
#     z = int(input("tell your element "))
#     l.append(z)
# print(l)
# m = int(input("enter the no"))
# x = l.count(m)
# print(x)

# Fibonacci series
# l = [0,1]
# m = l[0]
# b = l[1]
# q = int(input('enter the no'))

# filconni series
# for i in range(int(q)-2):
#     c = m+b
#     m = b
#     b = c
 
#     if c <=q:
#         l.append(c)
#     else:
#         break  
# print(l)

#write a program to find all the pairs whose sum is equal to the given no 
# l=[1,6,4,2,4,6,12,10]
# n=16
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==n:
#             print(l[i] ,'and ', l[j])

# C1 = int(input("enter the profit  of C1"))
# C2 = int(input("enter the profit  of C2"))
# C3 = int(input("enter the profit  of C3"))
# C4 = int(input("enter the profit  of C4"))


# say yes if the max is grater than other 3 
# maxx = max(C1,C2,C3,C4)
# summ = C1+C2+C3+C4
# t = summ - maxx
# if maxx>t:
#     print("YES ")
# else:
#     print("NO")

# l = []
# a = int(input("enter the no"))  #for no     
# for i in range(a):
#     z = int(input("tell your element "))
#     l.append(z)
# maxx = 0 
# index = 0 
# for  j in range(0 , len(l)):
#     if l[j] > maxx:
#         maxx = l[j]
#         index = j
# print(f"{maxx} found at {index}")
# summ = sum(l)
# t = summ - maxx
# if maxx > t:
#     print("yes")
# else:
#     print("no")


# a = input("the string")
upper_case = 0
lower_case = 0
numeric_values = 0
special_character = 0
for  character in a:
    if character.islower():
        lower_case = lower_case +1 
    elif character.isupper():
        upper_case = upper_case + 1
    elif character.isdigit():
        numeric_values = numeric_values + 1
    else:
        special_character = special_character +1
# print( f"upperr count {upper_case}")
# print(f"the lower case is {lower_case}")
# print(f"the numeric no is {numeric_values}")
# print(f"the special character is {special_character}")

