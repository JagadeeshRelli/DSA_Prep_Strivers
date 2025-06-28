# https://takeuforward.org/data-structure/sum-of-first-n-natural-numbers/

# Example 1:
# Input: N=5
# Output: 15
# Explanation: 1+2+3+4+5=15

# Example 2:
# Input: N=6
# Output: 21
# Explanation: 1+2+3+4+5+6=15



# n=int(input())

# sm=0
# i=1
# while(i<=n):
#     sm+=i 
#     i+=1
# print(sm)

# to o(n)
# so o(1)




n=int(input())

def recurr(i,n,sm):
    if(i>n):
        return sm
    return recurr(i+1,n,sm+i)

tmp=recurr(1,n,0)
print(tmp)

to o(n) 
so o(n)

