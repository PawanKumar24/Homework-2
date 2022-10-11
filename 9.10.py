# Pawan Kumar
# ID: 2046222
import csv

fileName = input()
with open(fileName, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        words = row
duplicates = list(dict.fromkeys(words))
length = len(duplicates)
for i in range(length):
    print(duplicates[i], words.count(duplicates[i]))