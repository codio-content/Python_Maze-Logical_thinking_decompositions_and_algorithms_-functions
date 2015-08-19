
def hitEnergyEvent():
  newScore = calcScore()
  showMessage('The new score is : ' + str(newScore) )

def hitMonsterEvent():
  showMessage('The new score is : ' + str(calcScore()) )

def calcScore():
  energy = getEnergy()
  steps = getSteps()
  score = energy * 5 / steps
  setScore(score)
  return score
