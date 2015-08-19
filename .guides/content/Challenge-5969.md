
{Check It!|assessment}(test-1728655712)

|||guidance
## Solution
Note that `energy += 5` is shorthand for `energy = energy + 5`.

```python
def hitMonsterEvent():
  energy = getEnergy()
  energy -= 5
  setEnergy(energy)
  calcScore()

def hitEnergyEvent():
  energy = getEnergy()
  energy += 5
  setEnergy(energy)
  calcScore()

def calcScore():
  energy = getEnergy()
  steps = getSteps()
  score = energy*5/steps
  setScore(score)
```
|||

## Take note
If you have solved this challenge, you can see one of the really great things about functions.

**A function can be called lots of times from many places.**

This is extremely important for these 2 reasons

1. You only have to write code once rather than writing the same code in lots of places.
2. It actually makes the code much neater and easier to read, so even if you only use it once, it makes the code much more readable.

