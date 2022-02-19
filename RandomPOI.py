def findRandomPOI(amountCharges):
  XTotal = 0
  YTotal = 0
  pointToChargeX = [0,0,0,0,0]
  pointToChargeY = [0,0,0,0,0]
  pointToCharge = [0,0,0,0,0]
  angleToPoint = [0,0,0,0,0]
  electricField = [0,0,0,0,0]
  opp = [0,0,0,0,0]
  adj = [0,0,0,0,0]
  XComponent = [0,0,0,0,0]
  YComponent = [0,0,0,0,0]

  pointY = random.uniform(-10,10)*10**-2
  pointX = random.uniform(-10,10)*10**-2
  calcDist(pointY, pointX, amountCharges)
  calcElectricField(amountCharges)
  calcAngle(amountCharges, pointY, pointX)
  XTotal = calcXComponent(amountCharges, XTotal)
  YTotal = calcYComponent(amountCharges, YTotal)
  electricFieldNet, angle = finalCalc(YTotal, XTotal)
  output(electricFieldNet, angle, pointY, pointX)

def findRandomCharge():
  for index in range(5):
    chargeXPosition[index] = random.uniform(-10,10)*10**-2
    chargeYPosition[index] = random.uniform(-10,10)*10**-2
    chargeMagnitude[index] = random.uniform(-10,10)*10**-2
  outputRandom()
  pointToChargeX = [0,0,0,0,0]
  pointToChargeY = [0,0,0,0,0]
  pointToCharge = [0,0,0,0,0]
  angleToPoint = [0,0,0,0,0]
  electricField = [0,0,0,0,0]
  opp = [0,0,0,0,0]
  adj = [0,0,0,0,0]
  XComponent = [0,0,0,0,0]
  YComponent = [0,0,0,0,0]
  XTotal = 0
  YTotal = 0

  amountCharges = 5
  pointY, pointX = getPoint()
  calcDist(pointY, pointX, amountCharges)
  calcElectricField(amountCharges)
  calcAngle(amountCharges, pointY, pointX)
  XTotal = calcXComponent(amountCharges, XTotal)
  YTotal = calcYComponent(amountCharges, YTotal)
  electricFieldNet, angle = finalCalc(YTotal, XTotal)
  output(electricFieldNet, angle, pointY, pointX)

def outputRandom():
  index = 0
  while index < 5:
    print("Random charge " + str(index + 1) + " is at position (" + str(chargeXPosition[index]) + "," + str(chargeYPosition[index]) + ") with charge " + str(chargeMagnitude[index]))
    index += 1