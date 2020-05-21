'''test_str= "geeks are the best website"
print("the original string is:",test_str)

test_dict = { 'geeks' : 3, 'best' : 5 }

for key in test_dict:
    if key in test_str.split(' '):
        test_str = test_str.replace(key," ")
print("string after replace is:"+ str(test_str))  #code 1'''

# 2nd solution

test_str = "geeks are the best"
print("the original string is:",test_str)

test_dict = { 'geeks' : 3, 'best': 5 }

temp = test_str.split(' ')
temp1 = [ word for word in temp if word.lower() not in test_dict ]
res = ' '.join(temp1)

print("string after remove\n"+str(res))