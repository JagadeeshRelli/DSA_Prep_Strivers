#https://takeuforward.org/pattern/pattern-11-binary-number-triangle-pattern/


# n=int(input())



# def recurr(i,n):
#     if(i==n):
#         return 

#     if(i%2==0):
#         st=1
#         cnt=0
#         for j in range(i+1):
#             if(cnt%2==0):
#                 print(st,end=" ")
#             else:
#                 print(st-1,end=" ")
#             cnt+=1
#         print()
#     else:
#         st=0
#         cnt=0
#         for j in range(i+1):
#             if(cnt%2==0):
#                 print(st,end=" ")
#             else:
#                 print(st+1,end=" ")
#             cnt+=1
#         print()
#     recurr(i+1,n)


# recurr(0,n)







# to o(n**2)
# so o(n)

        






n=int(input())


def recurr(i,n):
    if(i>n):
        return 

    st=1 if i%2==0 else 0    
    for j in range(i+1):
        print(st if j%2==0 else 1-st,end=" ")
    print()

    recurr(i+1,n)

recurr(0,n)





