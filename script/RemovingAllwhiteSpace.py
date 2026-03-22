import re
String= "c o D E"
spaces=re.compile(r'\s+')
result=re.sub(spaces,"",String)
print(result)