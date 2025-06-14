#https://takeuforward.org/pattern/pattern-20-symmetric-butterfly-pattern/

# *          *
# **        **
# ***      ***
# ****    ****
# *****  *****
# ************
# *****  *****
# ****    ****
# ***      ***
# **        **
# *          *



n=int(input())

def recurr(i,n):
    if(i>n):
        return 

    print("*"*i+"  "*(n-i)+"*"*i,end="")
    print()

    recurr(i+1,n)
    i-=1
    print("*"*i+"  "*(n-i)+"*"*i,end="")
    print()



recurr(1,n+1)




so o(n)
to o(n**2)