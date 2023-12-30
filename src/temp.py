test_str = 'password'
 
# printing original string
print("The original string is : " + str(test_str))
 
# Using any() to check for any element to be uppercase
res = any(ele.isupper() for ele in test_str)
 
# printing result
print("Does String contain uppercase character : " + str(res))
