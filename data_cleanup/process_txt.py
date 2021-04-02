import os
import re

filename = "thechroniclesofnarnia"

with open(filename + ".txt", 'r') as f:
	file_input = f.readlines()

train_doc = []
val_doc = []
for cnt, line in enumerate(file_input):
	if cnt <= len(file_input) * 0.90:
		train_doc.append(line)
	else:
		val_doc.append(line)

f = open('train_' + filename + '.txt', "w+")
count = 0
for line in train_doc:
	count = count + 1
	f.write(str(line))
	f.write("\n")

f.close()
print(count)

f = open('val_' + filename + '.txt', "w+")
count = 0
for line in val_doc:
	count = count + 1
	f.write(str(line))
	f.write("\n")

f.close()
print(count)
