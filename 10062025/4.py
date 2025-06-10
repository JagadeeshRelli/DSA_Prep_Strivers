# https://takeuforward.org/pattern/pattern-18-alpha-triangle-pattern/


# F
# E F
# D E F
# C D E F
# B C D E F
# A B C D E F



n=int(input())

for i in range(n):
    tmp=65
    for j in range(n-i-1,n,1):
        print(chr(tmp+j),end="")
    print()

so o(1)
to o(n**2)