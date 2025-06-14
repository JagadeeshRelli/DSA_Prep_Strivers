#https://takeuforward.org/pattern/pattern-21-hollow-rectangle-pattern/


# ******
# *    *
# *    *
# *    *
# *    *
# ******

# n=int(input())

# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n)
#     else:
#         print("*"+" "*(n-2)+"*")

# so o(1)
# to o(n**2)



n=int(input())

def recurr(i,n):

    if(i>(n//2)):
        return 

    if(i==1 ):
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")
    recurr(i+1,n)
    #print(i)
    if(n%2==0):
        i-=1
    #print(i)
    if(i==1 ):
        print("*"*n)
    elif(i>1):
        print("*"+" "*(n-2)+"*")


recurr(1,n+1)


so o(n)
to o(n**2)