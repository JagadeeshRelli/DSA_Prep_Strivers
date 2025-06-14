# https://takeuforward.org/pattern/pattern-19-symmetric-void-pattern/

# ************
# *****  *****
# ****    ****
# ***      ***
# **        **
# *          *
# *          *
# **        **
# ***      ***
# ****    ****
# *****  *****
# ************




# n=int(input())


# for i in range(n,0,-1):
#     print("*"*i+"  "*(n-i)+"*"*i,end="")
#     print()
# for i in range(1,n+1):
#     print("*"*i+"  "*(n-i)+"*"*i,end="")
#     print()

# so o (1)
# to o(n**2)





n=int(input())

def recurr(i,n):
    if(i<1):
        return 
    print("*"*i+"  "*(n-i)+"*"*i,end="")
    print()

    recurr(i-1,n)

    print("*"*i+"  "*(n-i)+"*"*i,end="")
    print()

recurr(n,n)



so o(n)
to o(n**2)