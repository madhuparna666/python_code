test_str = "geeksarebest"
print("THE ORIGINAL STRING IS:",test_str)

temp = str.maketrans("geeks","weeks")
test_str = test_str.translate(temp)

print("strings after swap:"+str(test_str))