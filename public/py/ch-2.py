
def hitEnergyEvent():
  energy = getEnergy()
  energy += 5
  setEnergy(energy)

def hitMonsterEvent():
  energy = getEnergy()
  energy -= 5
  setEnergy(energy)

def calcScore(factor):
  energy = getEnergy()
  steps = getSteps()
  score = energy * factor / steps
  setScore(score)
