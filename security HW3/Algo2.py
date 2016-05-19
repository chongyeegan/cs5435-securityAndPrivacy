import itertools
import sys
import random
import numpy as np

top100 = [
    '123456',
    '12345',
    '123456789',
    'password',
    'iloveyou',
    'princess',
    '1234567',
    'rockyou',
    '12345678',
    'abc123',
    'nicole',
    'daniel',
    'babygirl',
    'monkey',
    'lovely',
    'jessica',
    '654321',
    'michael',
    'ashley',
    'qwerty',
    '111111',
    'iloveu',
    '000000',
    'michelle',
    'tigger',
    'sunshine',
    'chocolate',
    'password1',
    'soccer',
    'anthony',
    'friends',
    'butterfly',
    'purple',
    'angel',
    'jordan',
    'liverpool',
    'justin',
    'loveme',
    'fuckyou',
    '123123',
    'football',
    'secret',
    'andrea',
    'carlos',
    'jennifer',
    'joshua',
    'bubbles',
    '1234567890',
    'superman',
    'hannah',
    'amanda',
    'loveyou',
    'pretty',
    'basketball',
    'andrew',
    'angels',
    'tweety',
    'flower',
    'playboy',
    'hello',
    'elizabeth',
    'hottie',
    'tinkerbell',
    'charlie',
    'samantha',
    'barbie',
    'chelsea',
    'lovers',
    'teamo',
    'jasmine',
    'brandon',
    '666666',
    'shadow',
    'melissa',
    'eminem',
    'matthew',
    'robert',
    'danielle',
    'forever',
    'family',
    'jonathan',
    '987654321',
    'computer',
    'whatever',
    'dragon',
    'vanessa',
    'cookie',
    'naruto',
    'summer',
    'sweety',
    'spongebob',
    'joseph',
    'junior',
    'softball',
    'taylor',
    'yellow',
    'daniela',
    'lauren',
    'mickey',
    'princesa']

honeywords = []
comb = []
words = []
password = []
p1 = []
p2 =  []
p3 = []
finalWord = []
FW = []
a = int(sys.argv[1])
inputfile = sys.argv[2]
outputfile = sys.argv[3]
with open(inputfile) as f:
  for line in f:
      check = any(c.isalpha() for c in line)
      x = random.randint(0, a)
      line = line.replace("\n", "")
      if(check == True):
      
        comb = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in line)))
        password = random.sample(top100, 3)
        
        chk = any(c.isalpha() for c in password[0])
        if chk == True:
         p1 = np.repeat((map(''.join, itertools.product(*((c.upper(), c.lower()) for c in password[0])))),1000)
         w1 = random.sample(p1,a)
        else:
         w1 = p1
        chk = any(c.isalpha() for c in password[1])
        if chk == True:
         p2 = np.repeat((map(''.join, itertools.product(*((c.upper(), c.lower()) for c in password[1])))),1000)
         w2 = random.sample(p2,a)
        else:
         w2 = p2
        chk = any(c.isalpha() for c in password[2])
        if chk == True:
         p3 = np.repeat((map(''.join, itertools.product(*((c.upper(), c.lower()) for c in password[2])))),1000)
         w3 = random.sample(p3,a)
        else:
         w3 = p3
	
	A = np.repeat(comb, 1000)

        words = random.sample(A, a)
        
        x = random.randint(0,a)
        for i in range(0,x):
          honeywords.append(words[i] + str(random.randint(60, 99)))
          honeywords.append(w1[i] + str(random.randint(60, 99)))
          honeywords.append(w2[i] + str(random.randint(60, 99)))
          honeywords.append(w3[i] + str(random.randint(60, 99)))
        for i in range(x,a):
          honeywords.append(str(random.randint(60, 99)) + words[i])
          honeywords.append(str(random.randint(60, 99)) + w1[i])
          honeywords.append(str(random.randint(60, 99)) + w2[i])
          honeywords.append(str(random.randint(60, 99)) + w3[i])

        finalWord = random.sample(honeywords, a)
        finalWord.append(line + str(random.randint(60, 99)))
        FW = random.sample(finalWord, len(finalWord))
        print FW 
        f = open(outputfile, "a")
        f.write(str(FW)+"\n")
        f.close()
        honeywords[:] = []
      else:
        password = random.sample(top100, 3)
        chk = any(c.isalpha() for c in password[0])
        if chk == True:
         p1 = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in password[0])))
         w1 = random.sample(set(p1),a)
        else:
         w1 = p1
        chk = any(c.isalpha() for c in password[1])
        if chk == True:
         p2 = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in password[1])))
         w2 = random.sample(set(p2),a)
        else:
         w2 = p2
        chk = any(c.isalpha() for c in password[2])
        if chk == True:
         p3 = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in password[2])))  
         w3 = random.sample(set(p3),a)
        else:
         w3 = p3
        x = random.randint(0,a)
        for i in range(0,x):
          honeywords.append(str(line) + str(random.randint(60, 99)))
          honeywords.append(w1[i] + str(random.randint(60, 99)))
          honeywords.append(w2[i] + str(random.randint(60, 99)))
          honeywords.append(w3[i] + str(random.randint(60, 99)))
        for i in range(x,a):
          honeywords.append(str(random.randint(60, 99)) + str(line))
          honeywords.append(str(random.randint(60, 99)) + w1[i])
          honeywords.append(str(random.randint(60, 99)) + w2[i])
          honeywords.append(str(random.randint(60, 99)) + w3[i])

        finalWord = random.sample(honeywords, a)
        finalWord.append(line + str(random.randint(60, 99)))
        FW = random.sample(finalWord, len(finalWord))
        print FW 
        f = open(outputfile, "a")
        f.write(str(FW)+"\n")
        f.close()
        honeywords[:] = []

