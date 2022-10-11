# Pawan Kumar
# ID: 2046222
from datetime import datetime

validDates = []
file = 'inputDates.txt'

with open(file,"r") as fin:
    lastval = fin.read().split('\n')
    for val in lastval:
        try:
            myval = datetime.strptime(val, '%B %d, %Y')
            validDates.append(myval)
        except Exception:
            pass

output = open("parsedDates.txt", "w")

for val in validDates:
    output.write(f'{val.month}/{val.day}/{val.year}\n')
    print(f'{val.month} - {val.day} - {val.year}')

output.close()