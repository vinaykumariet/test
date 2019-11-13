#1)Write a Program to print all prime numbers up to a given number?

low=5
high=11
for num in range(low,high+1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  



# program to check no is prime or not

number=4

if number >1:
    for i in range(2,number):
        if number % i ==0:
            print("no is not prime")
            break
    else:
        print ("no is prime")    

else:
    print("no is not prime")


# program to check if a string is palindrome or not without loop   


teststring="malayalam"

newstring=teststring[::-1]
if teststring==newstring:
    print("string is palindrome")
else:
    print("string is not palindrome")


# program to check if a string is palindrome or not using loop  
# a=[1,2,3]
# b=a
# c=a[:]
# print(b==a)
# print(b is a)
# print(c== a)
# print(c is a)


# a=[6,4,34]
# b=[6,4,34]
# print(hex(id(a)))
# print(hex(id(b)))

# weekdays = 'abaccde'
# print([[x,weekdays.count(x)] for x in set(weekdays)])

# names = ['Chris', 'Jack', 'John', 'Daman']
# print(names[-1][-1])


names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

#print((names1))
# print(id(names2))
# print(names3)



# sum = 0
# for ls in (names1, names2, names3):
# if ls[0] == ‘Alice’:
# sum += 1
# if ls[1] == ‘Bob’:
# sum += 10

# print sum



# a=[]
# n= int(input('Enter the number of elements in list:'))
# for x in range(0,n):
#     element=int(input("Enter element" + str(x+1) + ":"))
#     a.append(element)
# temp=a[0]
# a[0]=a[n-1]
# a[n-1]=temp
# print("New list is:" ,a, end="")


# sum1=0
# num=int(input("Enter a number:"))
# temp=num
# while(num):
#     i=1
#     f=1
#     r=num%10
#     while(i<=r):
#         f=f*i
#         i=i+1
#     sum1=sum1+f
#     num=num//10
# if(sum1==temp):
#     print("The number is a strong number")
# else:
#      print("The number is not a strong number")

# n=int(input("Enter any number: "))
# a=list(str(n))
# print(a);




def sq(a):
     return a*a


def cube(a):
    return a*a*a


l1=[sq,cube]  



for i in range(1,7):
    res=list(map(lambda x: x(i), l1))
    print (res)

# l1=[1,2,3,4,5,6]
# res=list(map(lambda x:x*x,l1))
# print (res)  

txt = "Hello, and welcome to my world."

# x = txt.islower()
# print(x)

# txt = "I love apples, apple are my favorite fruit"

# x = txt.count("apple")

# print(x)

# txt = "Hello, welcome to my world."

# x = txt.find("wehhlcome")

# print(x)
import pickle

# f=open("abc.txt","wb")
# lid=['ddd','dfyrt','fhfh','gfjuyh']
# pickle.dump(lid,f)


# f=open("abc.txt","rb")
# lid=['ddd','dfyrt','fhfh','gfjuyh']
# print(pickle.load(f))



# print(f.write(lid))
# for i in f:
#     print(i,end="")
# print(f.write("fdrfd \n"))
# f.close()


# str="abcdefgyuio"
# print(str[5::2])

# ''' new'''

# local_var=10
# def a(n):
#     local_var=local_var+10
#     print(local_var)
#     print(n)


# def b():
#     local_var=10
#     def c():
#         global local_var
#         local_var=5
#     print(f"befor assignmnet {local_var}")
#     c()
#     print(f"after assignmnet {local_var}")


# # b("dddddddd")
# b()

# def factori(n):
#     fact=1
#     for i in range(n):
#         fact=fact*(i+1)
#     return fact    

# fact_number=int(input("Enter any number"))
# print(factori(fact_number))


# x = ('key1', 'key2', 'key3')
# y = 0,1

# thisdict = dict.fromkeys(x, y)

# print(thisdict)


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# car_pop= car.pop("model")

# print(car)

# print(car_pop)

# lisst=[]

# lisst.insert(0,5)
# lisst.insert(1,10)
# # lisst.insert(0,6)

# print (lisst)
# n = int(input())
# arr = list(map(int, input().split()))
# rmdu=[]
# # if not rmdu:
# #   min_value=111111111111110
# # else:
# #  min_value=rmdu[0]
# for i in arr:
#     if i not in rmdu:
#         rmdu.append(i)
#         # if i < min_value:
#         #      min_value=i     
        



# # print(rmdu)
# # print(min_value)
# min_value=rmdu[0]
# max_value=rmdu[0]
# for m in arr:
#     if m < min_value:
#          min_value=m   

# # print(min_value)

# maxs= min_value
# secont_max= min_value
# minx= 1000000000000000000
# secont_min= 1000000000000000000
# # print(maxs)
# # print(secont_max)

# for k in rmdu:
#     if k > maxs:
#         secont_max=maxs
#         maxs=k
#     elif secont_max<k:
#         secont_max=k
#     if k < minx:
#         secont_min=minx
#         minx=k
#     elif(secont_min>k):
#         secont_min=k    

         

# print(maxs,secont_max,minx,secont_min)

# subject_name=[]
# subject_score=[]
# for i in range(int(input())):
#         name = input()
#         score = float(input())
#         subject_name.append(name)
#         subject_score.append(score)


# rank=dict(zip(subject_name,subject_score))

# second_min=subject_score[0]
# minxcc=subject_score[0]

# # for name,score in rank.items():
# #     if score<min:
# #         second_min=min        
# #         min=score
# #     elif second_min > score:
# #         second_min=score
# print(subject_score)
# for k in subject_score:
#     if k < minxcc:
#         second_min=minxcc
#         minxcc=k
#     elif(!(minxcc<second_min) && k >second_min ):    
#         second_min=k
     
# print(second_min)

# nameee=[]
# for key,value in rank.items():
#     if value==second_min:
#         nameee.append(key)
# print("\n".join(sorted(nameee)))

# def calculateAverage(args):
#     argCount = len(args)
#     if argCount > 0 :
#         sumOfNums = 0
#     # Iterate over all the arguments and calculate average
#     for elem in args :
#         sumOfNums += elem
#     a =sumOfNums / argCount
#     return "%.2f" % round(a,2)




# n = int(input())
# student_marks = {}
# for i in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores

# query_name = input()
# score_list= student_marks[query_name]
# print(calculateAverage(score_list))  



import numpy
# m = list(map(int,input().split()))
# k = [list(map(int,input().split())) for i in range(m[0])]
# #print k
# n = numpy.array(k)
# # print (numpy.transp
# ose(n))
# # print (n.flatten())

# # print(m)
# print(k)
# print(n)


# m= list(map(int,input().split()))

# # for i in range(m[0] + m[1]):
# array_1=numpy.array([list(map(int,input().split())) for j in range(m[0])])
# array_2=numpy.array([list(map(int,input().split())) for k in range(m[1])])



# print (numpy.concatenate((array_1, array_2)))
  


# m=list(map(int,input().split()))


# k = map(int,input().split())
# print (numpy.zeros(k,dtype = numpy.int))
# print (numpy.ones(k,dtype = numpy.int))



# nums = tuple(map(int, input().split()))


# print (numpy.zeros((nums), dtype = numpy.int))
# print (numpy.ones(nums, dtype = numpy.int))

    
    # print (numpy.zeros((m[1],m[2]), dtype = numpy.int))
    # print  (numpy.ones((m[1],m[2]), dtype = numpy.int)) #Type changes to int
#    print (numpy.zeros(m[1],m[2]), dtype = numpy.int)
#    print (numpy.ones(m[1],m[2]), dtype = numpy.int) 

# letters = "asdfHRbySFss"
# uppers = [l.lower() if l.isupper() else l.upper() for l in letters]

# print ("".join(uppers))

# k = input()
#     isaln=None
#     isal=None
#     isdi=None
#     islo=None
#     isup=None
#     for s in k:
#         if s.isalnum():
#             isaln=s.isalnum()
#         if s.isalpha():
#             isal=s.isalpha()
#         if s.isdigit():
#             isdi=s.isdigit()
#         if s.islower():
#             islo=s.islower()
#         if s.isupper():
#             isup=s.isupper()



    
#     print(isaln)
#     print(isal)
#     print(isdi)
#     print(islo)
#     print(isup)

# s = input()
# for test in ('isalnum()', 'isalpha()', 'isdigit()', 'islower()', 'isupper()'):
#     print(any(eval("c." + test ) for c in s))


# def main():
#     # Replace all ______ with rjust, ljust or center. 

#     thickness = int(input())  # This must be an odd number
#     c = 'H'
    
#     # Top Cone
#     for i in range(thickness):
#         print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
    
#     # Top Pillars
#     for i in range(thickness + 1):
#         print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
    
#     # Middle Belt
#     for i in range((thickness + 1) // 2):
#         print((c * thickness * 5).center(thickness * 6))    
    
#     # Bottom Pillars
#     for i in range(thickness + 1):
#         print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))    
    
#     # Bottom Cone
#     for i in range(thickness):
#         print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))  

# if __name__ == '__main__':
#     main()

# def wrap(string, max_width):
#     lis=[]
#     first=0
#     second=max_width
#     for i in range(len(string)):
#         if i %max_width ==0:
#             lis.append(string[first:second])
#             first=second
#             second+=max_width

#     return "\n".join(lis)
    

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)  

# def print_formatted(number):
# width=len(bin(number)[2:])
# for i in range(1,number+1):
#     deci=str(i)
#     octa=oct(i)[2:]
#     hexa=(hex(i)[2:]).upper()
#     bina=bin(i)[2:]
#     print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))






# def solve(s):
#     fistname=s[:].split()
#     return " ".join([x.capitalize() for x in fistname]) 
    

#     # return " ".join(fistname.capitalize(),lastname.capitalize())


# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = solve(s)
#     print(type(result))
#     print(result)
    # fptr.write(result + '\n')

    # fptr.close()

# string="fggfjghkjhkjlkj"
# i=iter(string)
# print(next(i))



# def testProc(n = []):
#     print (n)

# testProc([1, 2, 3]) # Explicitly passing in a list
# testProc()  # Using a default empty list    

# inyString = "Hello World"
# for i in  inyString:
#     if i == "":
#         continue
#     print(i ,end="")


n = 10
# first two terms
n0 = 0
n1 = 1
#Count
x = 0
# check if the number of terms is valid
# if n <= 0:
#    print("Enter positive integer")
# elif n == 1:
#    print("Numbers in Fibonacci sequence upto",n,":")
#    print(n0)
# else:
#    print("Numbers in Fibonacci sequence upto",n,":")
#    while x < n:
#        print(n0,end=', ')
#        nth = n0 + n1
#        n0 = n1
#        n1 = nth
#        x += 1

# x = ['ab','cd']
# print(list(map(list, x)))
rng = 9
m=0
for i in range(rng):
    
    for j in range(rng-i):
        print(' ',end="")
    
    tm = (rng-j)+m   
    for k in range(tm):
        print('*',end="")    
    m+=1
    print('\n')