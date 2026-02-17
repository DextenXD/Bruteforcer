import random

code = random.randint(0, 100)

with open("wordlist.txt") as data :
  content = data.read()

wordlist = list(map(int, content.split(",")))

for x in wordlist:
  if x == code:
    print("Succes")
