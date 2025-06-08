#https://takeuforward.org/pattern/pattern-8-inverted-star-pyramid/



# n=int(input())


# for i in range(n,0,-1):
#     print(" "*(n-i)+"*"*(2*i-1))

# so= o(1)
# to = o(n)








# n=int(input())

# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()


# so=o(1)
# to=o(n**2)







# n=int(input())


# def recurr(i,n):
#     if(i==0):
#         return 
#     print(" "*(n-i)+"*"*(2*i-1))
#     recurr(i-1,n)

# recurr(n,n)


# so=o(n)
# to=o(n)









n=int(input())


def recurr(i,n):
    if(i==0):
        return 
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()

    recurr(i-1,n)

recurr(n,n)



so=o(n)
to=o(n**2)





# *********
#  *******
#   *****
#    ***
#     *