#this module is used for searching 
#\w is used for words 
#{2,3}$ gives 1 if it is present in exactly at 2 or 3 positions
#a = "^[a-z 0-9]+[@][a-z]+[.][a-z]{2,3}$"    we can use this instead a = "^[a-z 0-9]+[@]\w+[.]\w{2,3}$" because \w gives right if we enter capital letter also.
import re
a = "^[a-z 0-9]+[@][a-z]+[.][a-z]{2,3}$"   
r = "^[a-z 0-9]+[@][a-z]+[.][a-z]+[.][a-z]{2,3}$"   
b = input()

if re.search(a,b):

    print("right email")
elif re.search(r,b):
    print("right email")
else:
    print("shut your fuck up")
 


    