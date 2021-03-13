import re
s = "peter@tutorial.com"
match = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', s, re.I)
print (match.group())


