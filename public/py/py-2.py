
def calcScore(factor):
  energy = getEnergy()
  steps = getSteps()
  score = energy * factor / steps
  setScore(score)
