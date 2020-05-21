test_str = "geeksforgeeks_is_best"
print("the original string is:",test_str)

res = test_str.replace("_"," ").title().replace(" ","")  # sol:1 ; title func. & replace func
print("string after changing snakecase:\n"+str(res))

# solution 2 using capwords() & replace() func.

#import string
#test_str = "geeksforgeeks_is_best"
#print("the original string is:",test_str)

#res = string.capwords( test_str.replace("_"," ").replace(" ",""))
#print("string after changeing case:\n"+str(res))