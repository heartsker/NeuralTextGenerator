import random
import os

wordsCount = 100

linkers = ["So", "Also", "By the way", "Moreover"]
personal = ["I", "personaly I"]
like = ["like", "love", "prefer"]
code = ["to write programms", "to program", "to code", "to write code"]

file = open("text.txt", "w")


for i in range(0, wordsCount):
	sentence = random.choice(linkers) + random.choice(personal) + random.choice(like) + random.choice(code) + "."
	file.write(sentence)

file.close()

os.system("git add .")
os.system("git commit -m 'new file was generated!'")
os.system("git push")