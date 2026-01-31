# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode


import random
import string


def code(x):
	try:
		if( len(x) < 3):
			value=x[::-1]
			return value
		else:
			val=x[1:len(x)]+x[0]

			first3=random.choices(string.ascii_letters,k=3)
			last3=random.choices(string.ascii_letters,k=3)
			first=''
			last=''
			for i in first3:
				first= first+i
			for i in last3:
				last=last+i
			
			final=first+val+last
			return final
	except:
		print("Error occurred while coding")
		return 0
    
    
def decode(x):
    try:
    	if( len(x) < 3):
    		value=x[::-1]
    		return value
    	else:
    		val=x[-4]+x[3:len(x)-4]
    		return val
    	
    except:
    	print("Some error occurred while decoding")
    	return 0

choice = input("Do you want to code or decode ? ")
if choice.upper() == "CODE":
	val = input("Enter a word to code ")
	x = code(val)
	print(x)
	
elif choice.upper() == "DECODE":
	val = input("Enter a word to decode ")
	x=decode(val)
	print(x)
else:
	print("Please enter correct value : (Code/Decode) ")