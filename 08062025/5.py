#https://takeuforward.org/pattern/pattern-14-increasing-letter-triangle-pattern/




# n=int(input())

# tmp=65
# for i in range(n):
#     tmp=65
#     for j in range(i+1):
#         print(chr(tmp),end=" ")
#         tmp+=1
#     print()


# so o(1)
# to o(n**2)




n=int(input())

def recurr(i,n):
    if(i==n):
        return 
        
    tmp=65
    for j in range(i+1):
        print(chr(tmp),end=" ")
        tmp+=1
    print()
    recurr(i+1,n)

recurr(0,n)


# so o(n)
# to o(n**2)


# A 
# A B 
# A B C 
# A B C D 
# A B C D E 