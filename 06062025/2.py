#https://takeuforward.org/pattern/pattern-9-diamond-star-pattern/




# n=int(input())

# for i in range(1,n+1):
#     #print("hii")
#     print(" "*(n-i)+"*"*(2*i-1))
# for i in range(n,0,-1):
#     print(" "*(n-i)+"*"*(2*i-1))

# to=o(1)
# so=o(n)










# n=int(input())

# def genfunc(tmp,n):

#     if(tmp==0):
#         x=1
#         y=n+1
#         z=1
#     elif(tmp==1):
#         x=n
#         y=0
#         z=-1
#     else:
#         print("invalid")
#     for i in range(x,y,z):
#         #print(i)
#         print(" "*(n-i)+"*"*(2*i-1))

# genfunc(0,n)
# genfunc(1,n)


# to=o(n)
# so=o(1)









n=int(input())

def recurr(i,n):


    if(i==n):
        return 

    print(" "*(n-i)+"*"*(2*i-1))
    recurr(i+1,n)
    print(" "*(n-i)+"*"*(2*i-1))



recurr(1,n+1)


to=o(n**2)
so=o(n)






#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *