# marks = int(input("enter student marks :"))
# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# elif(marks >= 60 and marks < 70):
#     grade = "E"
# else:
#     grade = "you are fail"
# print("grade of the student = ", (grade))



# age = 55
# if(age >= 18):
#     if(age >= 80):
#         print("1cannot drive")
#     else:
#         print("can drive")
# else:
#     print("2cannot drive")


# num = input("enter your number : ")
# if (num %2 == 0):
#     print("print number is even")
# else:
#     print("number is odd").


# num1 = int(input("enter number one : "))
# num2 = int(input("enter number two : "))
# print (num1 + num2)

# square = float(input("enter square side : "))
# print ("square side", square * square)

# a = int(input("enter number one : "))
# b = int(input("enter number two : "))

# print ("average of the number is",(a + b)/2)

# a = int(input("enter number one : "))
# b = int(input("enter number two : "))
# print(a >= b)

# WAP to input user's first name & print its length
# user_name = input("enter your first name : ")
# print(len(user_name))

# # WAP to find the occurrence of '&' in a string
# var = "hi my name is ayush o am going to make lots of &&&&&&" 
# print(var.count("&"))

#WAP TO CHECK IF A NUMBER ENTERED BY THE USER IS ODD OR EVEN
# a = input("enter the number by user : ")
# if(a % 2 == 0):
#     print("number is even")
# else:
#     print("number is odd")

# LIST 
# marks = [92, 89, 88, 81, 73 ]
# print (marks)
# print(marks[0])
# print(marks[1])

# student = ["ayush   mishra", 99, "mumbai" ]
# print(student)
# print(type(student))
# student[0] = "piyush mishra"
# print(student)

# # SLICING
# marks = [92, 89, 88, 81, 73 ]
# print(marks[1 : 3])

# list = [20, 30, 10, 90, 80]
# list.append(60)
# print(list)

# list.sort()
# print(list)

# list.sort(reverse=True)
# print(list)

# list.reverse()
# print(list)

# list = ["banana", "litchi", "apple"]
# print(list.sort(reverse=True))
# print(list)

# list = [2, 3, 5, 4]
# list.insert(2, 10)
# print(list)

# # TUPLEs
# tup = (2, 3, 1, 8)
# print(type(tup))
# print(tup)

#tuple slicing
# tup = (1, 2, 3, 4)
# print(tup[1:4])

#tuple method
# tup = (2, 3, 1, 4, 4, 4, 4, 4, 4)
# print(tup.index(2))
# print(tup.index(4))
# print(tup.count(4))

# WAP TO ASK THE USER TO ENTER NAME OF THEIR 3 FAVORITE MOVIES & STORE THEM IN A LIST
# movies = []
# movie1 = input("enter your movie 1 : ")
# movie2 = input("enter your movie 2 : ")
# movie3 = input("enter your movie 3 : ")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)

# brother = []
# bro1 = input("enter brother name 1 : ")
# bro2 = input("enter brother name 2 : ")
# bro3 = input("enter brother name 3 : ")
# bro4 = input("enter brother name 4 : ")

# brother.append(bro1)
# brother.append(bro2)
# brother.append(bro3)
# brother.append(bro4)
# print(brother)


# WAP TO ASK THE USER TO ENTER NAME OF THEIR 3 FAVORITE MOVIES & STORE THEM IN A LIST
# movies = []
# movies.append(input("enter your movie 1 : "))
# movies.append(input("enter your movie 2 : "))
# movies.append(input("enter your movie 3 : "))

# print(movies)

# WAP TO CHECK IF A LIST CONTAIN A PALINDROME OF ELEMENTS. (NINT: USE COPY()METHOD)
# [1, 2, 3, 2, 1] [1, "abc", "abc" 1]
# list2 = [1, 2, 1]
# list1 = [1, 2, 3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("PALINDROME")
# else:
#     print("NOT PALINDROME")

# 2)
# list = ["m", "a", "a", "m"]
# copy_list = list.copy()
# copy_list.reverse()

# if(copy_list == copy_list):
#     print("PALINDROME")
# else:
#     print("NOT PALINDROME")

# 3)

# list1 = ["m", "o", "m", "o", "s"]
# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("PALINDROME")
# else:
#     print("NOT PALINDROME")

# WAP TO COUNT THE NUMBER OF STUDENT WITH THE "A" GRADE IN THE FOLLOWING TUPLE
#["C", "D", "A", "A", "B", "B", "A"]

# tup = ["C", "D", "A", "A", "B", "B", "A"]
# print(tup.count("A"))
# print(tup.count("B"))
# print(tup.count("C"))
# print(tup.count("D"))

# STORE THE ABOVE VALUES IN A LIST & SORT THEM FROM "A" TO "D"
# list = ["C", "D", "A", "A", "B", "B", "A"]
# list.sort()
# # print(list)


# DICTIONARY
# info = {
#     "name" : "ayush mishra",
#     "college" : "PVPIT",
#     "city" : "pune",
#     "age" : 20,
# }
# print(info["name"])
# print(info["college"])
# print(info["age"])

# info = {
#     "name" : "ayush",
#     "college" : "PVPIT",
#     "city" : "pune",
#     "age" : 20,
# }
# info["name"] = "ayush mishra",
# print(info["name"])

# NESTED DICTIONARY
# student = {
#     "name" : "ayush mishra",
#     "marks" : {
#         "phy" : 90,
#         "chem" : 93,
#         "math" : 98,
#     }
# }
# print(student["marks"]["chem"])

# DICTIONARY METHODS
# KEY METHOD
# student = {
#     "name" : "ayush mishra",
#     "marks" : {
#         "phy" : 90,
#         "chem" : 93,
#         "math" : 98,
#     }
# }
# print(list(student.keys()))
 
# VALUES METHOD
# student = {
#     "name" : "ayush mishra",
#     "marks" : {
#         "phy" : 90,
#         "chem" : 93,
#         "math" : 98,
#     }
# }
# print(student.values())

# ITEMS METHOD

# student = { 
#     "name" : "ayush mishra",
#     "subjects" : {
#         "math" : 90,
#         "phy" : 98,
#         "chem" : 90,
#     }
# }

# # print(student["name2"])
# print(student.get("name1"))

# print("hi")
# print("welcome to my program")
# print("ayush mishra")
# print("i am learning")
# print("python language")
# print("from apna college ")

# a = 10
# b = 100
# c = 20
# sum = a+b+c
# print (sum)

# UPDATE METHOD
# student = { 
#     "name" : "ayush mishra",
#     "subjects" : {
#         "math" : 90,
#         "phy" : 98,
#         "chem" : 90,
#     }
# }

# student.update({"city" : "mumbai"})
# print(list(student))


# hostel_1 = {
#     "hostel" : "boys",
#     "boys" : {
#         "first_yr" : "yash kulkarni",
#         "second_yr" : "ayush mishra",
#         "third_yr" : "akash",
#         "forth_yr" : "neeraj mali",
#         "girls" : {
#             "first_yr" : "mansi k",
#             "second_yr" : "neha",
#             "third_yr" : "xx",
#             "forth_yr" : "yy",

#         }
#     }
# }

# # print(list(hostel_1["boys"]))
# # print(hostel_1.values())

# hostel_1.update({"trans" : "mahesh"})
# print (hostel_1)

# SET IN PYTHON
# collection = {1, 2, 3, 4, "hello", "world", "world"}

# print(collection)
# print(type(collection))
# print(len(collection))

#LOOPS IN PYTHON 
# WHILE LOOPS
# count = 1
# while count <= 25:
#     print("hello")
#     count += 1 

# i = 1
# while i <= 100:
#     print ("hi bro" , i)
#     i += 1

# print (" hi ")
# a = 200
# while a >= 100:
#     print("now your value is small" ,a)
#     a -= 1

# print ("your loop is ended")

# q
# PRINT NUMBER FROM 1 TO 100
# a = 1 
# while a <= 100 :
#     print (a)
#     a += 1
# print ("hear is your numbers")

# PRINT NUMBER FROM 100 TO 1
# a = 100 
# while a >= 1 :
#     print (a)
#     a -= 1
# print ("hear is your numbers")

# PRINT THE MULTIPLICATION TABLE OF A NUMBER N
# num = int(input("enter your number :"))
# n = 1
# while n <= 10 :
#     print(num*n)
#     n += 1

# num = int(input("enter your table number : "))
# n = 1
# while n <= 10 :
#     print(num*n) 
#     n += 1

# num = int(input("enter your table number : "))
# n = 1
# while n <= 10 :
#     print(num/n) 
#     n += 1

# Q4
#PRINT THE ELRMENT OF THE FOLLOWING LIST USING A LOOP
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# nums =  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# idx = 0 
# while idx < len (nums):
#     print (nums[idx])
#     idx += 1

# names = ["yash", "ayush", "sarthak", "mahesh"]
# i = 0
# while i < len(names):
#     print(names[i])
#     i += 1

# Q 
# SEARCH FOR A NUMBER X IN THIS TUPLE USING LOOP :
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 36
# x = 49
# i = 0
# while i < len(tup):
#     if(tup[i] == x):
#         print("yooo we found the number", i)
#     i += 1


# BREAK
# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1

# print("end of the loop")

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 36

# i = 0
# while i < len (nums):
#     if(nums[i] == x):
#         print("found at idx ", i)
#         break
#     else :
#         print("finding....")
#         i += 1  

# i = 0 
# while i <= 5 :
#     if(i == 3):
#         i += 1 
#         continue
#     print(i)
#     i += 1

# heroes = ["ironman", "thor", "superman", "batman"]

# idx = 0
# while idx < len (heroes):
#     print(heroes[idx])
#     idx += 1

# SEARCH FOR A NUMBER X IN THIS TUPLE USING LOOP
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 100
# i = 0
# while i < len(num):
#     if(num[i] == x):
#         print("found at idx", i)
#     else: 
#         print("finding... ")
#     i += 1

# BREAK
# i = 1
# while i <= 5:
#     print(i)
#     if (i==3):
#         break
#     i += 1

# print("end of loop")

# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 4
# i = 0
# while i < len(num):
#     if(num[i] == x):
#         print("found at idx", i)
#         break
#     else: 
#         print("finding... ")
#     i += 1
# print("pg end ho gaya")

# CONTINUE
# i = 0
# while i <= 5 :
#     if(i == 3):
#         i += 1
#         continue
#     print(i)
# #     i += 1

# str = "ayush mishra"
# for char in str:
#     if(char == "y"):
#         print("y found")
#         break
#     print(char)
# else:
#     print("END")

# PRINT THE ELEMENTS OF THE FOLLOWING LIST USING A LOOP:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# x = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for el in x:
#     print(el)

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x = 100

# idx = 0
# for el in num:
#     if (el == x):
#         print("number found at idx", idx)
#     idx += 1

# name = ["ayush", "piyush", "shreyansh", "adarsh", "anand", "pawan", "jaja", "ayush"]


# idx = 0
# while idx < len (name):
#     print(name[idx])
#     idx += 1

# # RANGE
# for i in range (101):
#     print(i)

