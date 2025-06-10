#https://takeuforward.org/pattern/pattern-16-alpha-ramp-pattern/

# A 
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F


# n=int(input())
# tmp=65
# for i in range(1,n+1):
#     for k in range(i):
#         print(chr(tmp),end=" ")
#     tmp+=1
#     print()

# so o(1)
# to o(n**2)







# n=int(input())
# tmp=65


# for i in range(1,n+1):
#     print(chr(tmp)*i)
#     tmp+=1


# so o(1)
# to o(n**2)









n=int(input())

def recurr(i,n,tmp):

    if(i>n):
        return 
    print(chr(tmp)*i)
    recurr(i+1,n,tmp+1)

recurr(1,n+1,65)

so o(n)
to o(n**2)