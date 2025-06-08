#https://takeuforward.org/pattern/pattern-10-half-diamond-star-pattern/

n=int(input())


def recurr(i,n):
    if(i>n):
        return 
    
    print("*"*(i))

    recurr(i+1,n)

    print("*"*(i-1))


recurr(1,n+1)

to o(n**2)]
so o(n)