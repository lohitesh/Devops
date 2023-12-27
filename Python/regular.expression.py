import re

emaildata = "bharath <bharath@gmail.com>, nithya ,nithya@gmail.com>, bharata <bharata@gmail.com>"

res = re.search(r"bharath",emaildata)
print(res)

res = re.search("Bhar", emaildata)
print(res)

res = re.search("Bhar", emaildata, re.IGNORECASE)
print(res)


res = re.search(r"bharat[i, a]",emaildata)
print(res)


res = re.search(r"bhara[a-z]{2}",emaildata)

print(res)


res = re.search(r"bhar[a-z]",emaildata)
print(res)

res = re.search(r"bhar[a-z]+",emaildata)
print(res)

res = re.search(r"[A-za-z0-9_]+@[A-za-z0-9]+\.[a-z]+", emaildata)
print(res)


res = re.search(r"\w+@\w+\.\w+",emaildata)
print(res)

result = re.findall(r"(\w+)@(\w+)\.(\w+)",emaildata)
print(result, result[0])

result = re.findall(r"\w+@\w+\.\w+",emaildata)
print(result, result[0])

