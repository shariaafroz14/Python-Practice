### counting the white spaces in a string##
##digits, Letters, Spaces,
import re
name = 'python is 1'
digitCount=re.sub("[^0,9]","",name)
letterCount=re.sub("[^aZA-Z]","",name)
spaceCount= re.findall("[\s]",name)

print(len(digitCount))
print(len(letterCount))
print(len(spaceCount))
