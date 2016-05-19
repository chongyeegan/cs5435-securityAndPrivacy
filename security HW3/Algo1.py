import itertools
import sys
import random
import numpy as np

honeywords = []
comb = []
words = []
content = []
honey = []
a = int(sys.argv[1])
inputfile = sys.argv[2]
outputfile = sys.argv[3]

with open(inputfile) as f:
  for line in f:
      check = any(c.isalpha() for c in line)
      x = random.randint(0, a)
      line = line.replace("\n", "")
      if(check == True):
        
        comb = map(''.join, itertools.product( * ((c.upper(), c.lower()) for c in line)))
      	
	A = np.repeat(comb, 1000)

        words = random.sample(A, a)
        for i in range(0, x):
          honeywords.append(words[i] + str(random.randint(60, 99)))
        for i in range(x, a):
          honeywords.append(str(random.randint(60, 99)) + words[i])
      
        honeywords.append(line + str(random.randint(60, 99)))
        honey = random.sample(honeywords, len(honeywords)) 
        print honey
        f = open(outputfile, "a")
        f.write(str(honey)+"\n")
        f.close()
        honeywords[:] = []
      else:
        for i in range(0, x):
          honeywords.append(str(line) + str(random.randint(60, 99)))
        for i in range(x, a):
          honeywords.append(str(random.randint(60, 99)) + str(line))
      
        honeywords.append(line + str(random.randint(60, 99)))
        honey = random.sample(honeywords, len(honeywords))
        print honey
        f = open(outputfile, "a")
        f.write(str(honey)+"\n")
        f.close()
        honeywords[:] = []
