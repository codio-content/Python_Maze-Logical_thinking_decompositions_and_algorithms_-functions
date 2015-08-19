
{Check It!|assessment}(test-2646396945)

|||guidance
## Solution

```python
def hitEnergyEvent():
  energy = getEnergy()
  energy += 5
  setEnergy(energy)
  calcScore(6)

def hitMonsterEvent():
  energy = getEnergy()
  energy -= 5
  setEnergy(energy)
  calcScore(6)

def calcScore(factor):
  energy = getEnergy()
  steps = getSteps()
  score = energy * factor / steps
  setScore(score)
```
|||