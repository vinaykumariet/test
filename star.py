# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")
#     print("\n")

# print("second programme")
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print("\n")         

# n=5
# for i in range(n):
#     for k in range(n-i):
#         print(" ",end="")
#     for m in range(n-k):
#         print("*",end="")
#     print("\n")        
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print(" ",end="")
#     for m in range(n-j):
#         print("*",end="") 
#     print("\n")
# 
# n=5
# m=0
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
        
#     for k in range((n-j)+m):
#         print("*",end="")
#     m+=1         
#     print("\n")
# n=5
# m=1
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     temp=n*2-i-m
#     for k in range(temp):
#         print("*",end="")  
#     m+=1     
#     print("\n") 

# n=5
# m=0
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
        
#     for k in range((n-j)+m):
#         if k %2==0:
#           print("1",end="")
#         else:
#           print("0",end="")      
#     m+=1         
#     print("\n")
# 
n=9
m=4
for i in range(n):
    if i>0 and i<4 :
        for p in range(m-i):
            print(" ",end="")
        for t in range(m-p):
            print("*",end="") 
        print("\n")                
    else:
        a=n-i
        for j in range(a):
            print(" ",end="")
        for m in range(n-j):
            print("*",end="") 
        print("\n")    