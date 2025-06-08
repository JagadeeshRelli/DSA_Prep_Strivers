#https://takeuforward.org/pattern/pattern-13-increasing-number-triangle-pattern/


# n=int(input())

# temp=0
# for i in range(n):
#     for j in range(i+1):
#         print(temp+1,end=" ")
#         temp+=1
#     print()

# so o(1)
# to o(n**2)



n=int(input())

def recurr(i,n,temp):
    if(i==n):
        return 

    for j in range(i+1):
        print(temp,end=" ")
        temp+=1
    print()
    recurr(i+1,n,temp)

recurr(0,n,1)


so o(n)
to o(n**2)