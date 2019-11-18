import re
import numpy as np

print(re.match,"^a","abcd")

f = open("iris.data","r")
# Reads the data in as a sinlge string
data = f.read()
# Splits the string into an array of strings split at lint break
lines = re.split(r"\n+", data)

# I've no idea if these headings are correct
results=(["PW","PL", "SW", "SL", "Var"])
# Breaking down the lines to the individual data
for line in lines:
    if line != "":
        vals = re.split(r",",line)
        results.append(vals)
print(results)
f.close()
