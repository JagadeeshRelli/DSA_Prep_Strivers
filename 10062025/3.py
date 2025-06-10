#https://takeuforward.org/pattern/pattern-17-alpha-hill-pattern/


#      A     
#     ABA    
#    ABCBA   
#   ABCDCBA  
#  ABCDEDCBA 
# ABCDEFEDCBA



# n=int(input())
# tmp=65

# for i in range(1,n+1):
#     tmp=65
#     print(" "*(n-i-1),end="")

#     for j in range(i):
#         print(chr(tmp+j),end="")
#         #print("in j for loop ")
        
#     for k in range(i-1,0,-1):
#         print(chr(tmp+k-1),end="")
#         #print("in k for loop")
#         #tmp-=1
#     print(" "*(n-i-1),end="")
#     print()


# to o(n**2)
# so o(1)











# n=int(input())


# def recurr(i,n):
#     if(i>n-1):
#         return 

#     tmp=65
#     print(" "*(n-i-1),end="")
#     for j in range(i):
#         print(chr(tmp+j),end="")
#     for k in range(i-1,0,-1):
#         print(chr(tmp+k-1),end="")
#     print(" "*(n-i-1),end="")
#     print()

#     recurr(i+1,n)

# recurr(1,n+1)


# so o(n)
# to o(n**2)

