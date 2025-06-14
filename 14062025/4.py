#https://takeuforward.org/pattern/pattern-22-the-number-pattern/


# 6 6 6 6 6 6 6 6 6 6 6 
# 6 5 5 5 5 5 5 5 5 5 6 
# 6 5 4 4 4 4 4 4 4 5 6 
# 6 5 4 3 3 3 3 3 4 5 6 
# 6 5 4 3 2 2 2 3 4 5 6 
# 6 5 4 3 2 1 2 3 4 5 6 
# 6 5 4 3 2 2 2 3 4 5 6 
# 6 5 4 3 3 3 3 3 4 5 6 
# 6 5 4 4 4 4 4 4 4 5 6 
# 6 5 5 5 5 5 5 5 5 5 6 
# 6 6 6 6 6 6 6 6 6 6 6



# n=int(input())
# tmp=""
# for i in range(n,0,-1):
#     #print(i)
#     #print(tmp)
    
#     if(i==n):
#         print(str(n)*(n-1)+str(n)+str(n)*(n-1))
        
#     else:
#         tmp+=str(i+1)
#         print(tmp,end="")
#         print(str(i)*(2*i-1),end="")
#         print("".join(list(tmp)[::-1]),end="")
#         print()  
# #print("   ")
# tmp=tmp[:-1]
# for i in range(2,n+1):
#     #print(i)
#     #print(tmp)
    
#     if(i==n):
#         print(str(n)*(n-1)+str(n)+str(n)*(n-1))
        
#     else:
        
#         print(tmp,end="")
#         print(str(i)*(2*i-1),end="")
#         print("".join(list(tmp)[::-1]),end="")
#         print()   
#         tmp=tmp[:-1]    
    

# so o(n)
# to o(n**2)


n=int(input())

def recurr(i,n,tmp):
    if(i<1):
        return 
    if(i==n):
        print(str(n)*(n-1)+str(n)+str(n)*(n-1))
    
    else:
        tmp+=str(i+1)
        print(tmp,end="")
        print(str(i)*(2*i-1),end="")
        print("".join(list(tmp)[::-1]),end="")
        print() 
    recurr(i-1,n,tmp)
    tmp=tmp[:-1]
    i+=1

    if(i==n):
        print(str(n)*(n-1)+str(n)+str(n)*(n-1))
        
    elif(i<n+1):
        
        print(tmp,end="")
        print(str(i)*(2*i-1),end="")
        print("".join(list(tmp)[::-1]),end="")
        print()   
        tmp=tmp[:-1]      


recurr(n,n,"")


so o(n)
to o(n**2)