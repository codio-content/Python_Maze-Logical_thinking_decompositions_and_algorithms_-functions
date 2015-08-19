
{Check It!|assessment}(test-2150872117)

|||guidance
## Solution

```python
def hitEnergyEvent():
  setEnergy(getEnergy() + 5)
  setScore(calcScore())

def hitMonsterEvent():
  setEnergy(getEnergy() - 5)
  setScore(calcScore())

def calcScore():
  return getEnergy() * 5 / getSteps()
```
|||
