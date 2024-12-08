# Question 59
# l = []
# a = int(input("enter the no"))  #for no     
# for i in range(a):
#     z = input("tell your element ")
#     l.append(z)
# print(l)

# s = "helllo my name is harsh"
# s = s.split()
# print(s)

# s = "helllo my name is harsh"
# s = s.split("h")
# print(s)

# s = input("enter your string").split() #for string
# print(s)

#question 60
# l = [2,4,56,878,77,44]
# print(l[::-1])

#question 61
# l = [0,1]
# a = l[0]
# b = l[1]
# z = int(input('enter the no'))

# for i in range(int(z)-2):
#     c = a+b
#     a = b
#     b = c
#     l.append(c)
# print(l)

#question 62
# for loop
# l = [1 , -2 ,4,98,-6,88]
# print("the neg elements are")
# for i in l :
#     if i <0:
#         print(i , end = " ")
# print("\nyour positive no")
# for i in l :
#     if i >= 0:
#         print(i , end = " ")

#while
# a = 0
# while len(l) != a:
#     if l(a) < 0:
#         print(l[a])
#     a = a+1

# question 63
# l =[1,3,556,78,7990,87,67,56]
# l.sort()
# print(l[::-1])

# question 64 / 42
# a = int(input("how many no"))
# l = []
# for i in range(a):
#     z = int(input("tell your no"))
#     l.append(z)
# summ = 0
# for i  in range(len(l)):
#     if i != len(l)-1:
#         print(f"{l[i]} +" , end = " ")
#     summ = summ + l[i]
# print(f"{l[len(l)-1]} = {summ}")

# question 43
# l = [1,3,56,78,54,65,6,78,6]
# summ = 0
# for i in l :
#     summ = summ +i
# print(round(summ/len(l),2))

# print(round(sum(l)/len(l),2))

# a = sum(l)
# print(a)

#question 44
# l = [2,4,6,76,54,77,65,44]
# maxx = 0 
# index = 0 
# for i in range(0 , len(l)):
#     if l[i] > maxx:
#         maxx = l[i]
#         index = i
# print(f"{maxx} found at {index}")

#question 45
# l = [2,4,6,76,54,77,65,44]
# minn = l[0]
# index = 0 
# for i in range(0 , len(l)):
#     if l[i] < minn:
#         minn= l[i]
#         index = i
# print(f"{minn} found at {index}")

# #question 46
# l = [2,4,6,76,54,77,65,44,78,89,81]
# maxx = 0 
# maxx2 = 0 
# index = 0 
# index2 = 0 
# for i in range(0 , len(l)):
#     if l[i] > maxx:
#         maxx2 = maxx
#         maxx = l[i]
#         index2 = index
#         index = i
#     elif l[i] > maxx2 and l[i]< maxx:
#         maxx2 = l[i]
#         index2 = i

# print(f"{maxx2} at {index2}")

#question 47
# l = [2,445,6,77,67,865,45,3437,78] 
# # l.sort()
# # print(l)     continue vaps loop m laata h 
# flag = True
# for i in range(0,len(l)-2):
#     if l[i] <= l[i+1]:
#         continue
#     else :
#         print("your list is unsorted")
#         flag = False
#         break
# if flag == True :
#     print("my list is sorted")

#question  48( isme time jada lgega kyuki do list use ho rhi h toh time compexity ka use hoga)
l = [2,4,5,5,4,2]
# newlist = []
# for i in range(len(l)-1,-1,-1):
#     newlist.append(l[i])
# if newlist == l:
#     print("pallandromic list")
# else:
#     print("bag jaaaa")

#2 pointer use (less space) space and time complexity            
# v = len(l)-1     #index value of last 
# flag = True 
# for i in range(0,(len(l))//2):
#     if l[i] == l[v]:
#         v-= 1
        
#         continue
#     else:
#         print("not palandrome")
#         flag = False 
#         break
# if flag == True :
#     print("pallindrome")


# l = [i for i in range(10,21) if i%2 ==0]
# print(l)