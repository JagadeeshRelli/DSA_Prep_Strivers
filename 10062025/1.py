#https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/




# n=int(input())

# tmp=65

# for i in range(n,0,-1):
#     tmp=65
#     for j in range(i):
#         print(chr(tmp),end=" ")
#         tmp+=1
#     print()

# to o(n**2)
# so o(1)







n=int(input())


tmp=65


def recurr(i,n):
    if(i==0):
        return 
    
    tmp=65
    for k in range(i):
        print(chr(tmp),end=" ")
        tmp+=1
    print()

    recurr(i-1,n)

recurr(n,n)

so o(n)
to o(n**2)













# A B C D E F
# A B C D E
# A B C D
# A B C
# A B
# A