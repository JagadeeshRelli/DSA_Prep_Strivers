# https://takeuforward.org/data-structure/check-if-a-number-is-palindrome-or-not/

# Example 1:
#                 Input:N = 4554
               
#                 Output:Palindrome Number
                
#                 Explanation: The reverse of 4554 is 4554 and therefore it is palindrome number
                                        
#                 Example 2:
#                 Input:N = 7789                
                
#                 Output: Not Palindrome
                
#                 Explanation: The reverse of number 7789 is 9877 and therefore it is not 





# n=int(input())
# if(str(n)[::-1]==str(n)):
#     print(True)
# else:
#     print(False)

# to o(d**2) d-digits in the number 
# so o(d)




# n=int(input())

# cnt=-1
# tmp=n
# while(tmp):
#     tmp//=10
#     cnt+=1
# tmp=n
# tmpsm=0
# while(tmp):
#     tmpsm+=(tmp%10)*(10**cnt)
#     tmp//=10
#     cnt-=1
# print(tmpsm==n)


# to o(d logd)
# so o(d)




n=int(input())

rev=0 

while(n>rev):
    rev=(rev*10)+(n%10)
    n//=10
print(n==rev or n==rev//10)


to o(d/2) -> o(log n)
so o(1)