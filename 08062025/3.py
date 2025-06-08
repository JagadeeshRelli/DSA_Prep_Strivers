#https://takeuforward.org/pattern/pattern-12-number-crown-pattern/


# n=int(input())

# for i in range(n):
    
#     for j in range(i+1):
#         print(j+1,end="")
#     #print(" "*(2*n- (2*(i+1))),end="")
#     print("  "*(n- (i+1)),end="")
    
#     for k in range(i+1,0,-1):
#         print(k,end="")
#     print()

# to o(n**2)
# so o(1)


n=int(input())



def recurr(i,n):
    if(i==n):
        return 
    for j in range(i+1):
        print(j+1,end="")
    #print(" "*(2*n- (2*(i+1))),end="")
    print("  "*(n- (i+1)),end="")
    
    for k in range(i+1,0,-1):
        print(k,end="")
    print()

    recurr(i+1,n)

recurr(0,n)



so o(n)
to o(n**2)

