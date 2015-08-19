
energy = 0
score = 0 
steps = 1

def getEnergy():
  global energy
  return energy

def setEnergy(val):
  global energy
  energy = val
  
def setScore(val):
  global score
  score = val
 
def getSteps():
  global steps
  return steps

try:
  execfile('/home/codio/workspace/public/py/ch-1.py')
  
  hitEnergyEvent()
  if energy != 5 or score != 25:
    raise ValueError('incorrect values')
  
  energy = 6
  score = 0
  steps = 1  
  hitMonsterEvent()
  
  if energy != 1 or score != 5:
    raise ValueError('incorrect values')

  energy = 5
  score = 0
  steps = 1
  calcScore()
  
  if score != 25:
    raise ValueError('incorrect values')
    
  print 'well done'
  exit(0)
except (IOError, SyntaxError, ValueError) as e:
  pass
  
print 'Not quite right, try again!'
exit(1)
