# https://takeuforward.org/data-structure/count-digits-in-a-number/

#  Example 1:
#                 Input:N = 12345
               
#                 Output:5
                
#                 Explanation:  The number 12345 has 5 digits.
                                        
#                 Example 2:
#                 Input:N = 7789                
                
#                 Output: 4
                
#                 Explanation: The number 7789 has 4 digits.                   





# n=int(input())

# print(len(str(n)))

# to o(d**2) -- d-digits
# so o(1)




# n=int(input())


# cnt=0
# while(n):
#     n//=10
#     cnt+=1
# print(cnt)


# so o(1)
# to o(log10 n +1)




import math
n=int(input())

print(math.floor(1+math.log10(n)))

so o(1)
to o(1)
