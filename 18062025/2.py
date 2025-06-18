#https://takeuforward.org/maths/reverse-digits-of-a-number


    # Example 1:
    #             Input:N = 12345
               
    #             Output:54321
                
    #             Explanation: The reverse of 12345 is 54321.
                                        
    #             Example 2:
    #             Input:N = 7789                
                
    #             Output: 9877
                
    #             Explanation: The reverse of number 7789 is 9877.
								




# n=int(input())

# print("".join(list(str(n))[::-1]))

# so o(1)
# to o(d**2)
# d-digits





# n=int(input())

# print(str(n)[::-1])

# so o(1)
# to o(d**2) d-digits





# n=int(input())

# tmpstr=""
# while(n):

#     tmpstr+=str(n%10)
#     n//=10
# print(tmpstr)



# so o(d)
# to o(d**2) d- digits
    




n=int(input())

res=0

while(n):
    tmpp=n%10
    res=(res*10)+tmpp
    n//=10
print(res)

so o(d)
to o(log10 n +1)


