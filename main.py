import math
import random

#Resets all variables
k = 9*10**9
chargeXPosition = [0,0,0,0,0]
chargeYPosition = [0,0,0,0,0]
chargeMagnitude = [0,0,0,0,0]
pointToChargeX = [0,0,0,0,0]
pointToChargeY = [0,0,0,0,0]
pointToCharge = [0,0,0,0,0]
angleToPoint = [0,0,0,0,0]
electricField = [0,0,0,0,0]
opp = [0,0,0,0,0]
adj = [0,0,0,0,0]
XComponent = [0,0,0,0,0]
YComponent = [0,0,0,0,0]

#Runs all functions
def main():
  XTotal = 0
  YTotal = 0
  amountCharges = getAmountCharges()
  getCharges(amountCharges)
  pointY, pointX = getPoint()
  calcDist(pointY, pointX, amountCharges)
  calcElectricField(amountCharges)
  calcAngle(amountCharges, pointY, pointX)
  XTotal = calcXComponent(amountCharges, XTotal)
  YTotal = calcYComponent(amountCharges, YTotal)
  electricFieldNet, angle = finalCalc(YTotal, XTotal)
  output(electricFieldNet, angle, pointY, pointX)
  findRandomPOI(amountCharges)
  findRandomCharge()

#Determines how many charges will be added to the calculation
def getAmountCharges():
  amountCharges = int(input("How many charges do you want to have (Max of 5)?"))
  while amountCharges <= 0 or amountCharges > 5:
    print("Please enter a value between 1 and 5")
    amountCharges = int(input("How many charges do you want to have (Max of 5)?"))
  return amountCharges

#Gets the information for each charge
def getCharges(amountCharges):
  for index in range(amountCharges):
    chargeXPosition[index] = (float(input("Input charge x position in centimeters: "))*10**-2)
    chargeYPosition[index] = (float(input("Input charge y position in centimeters: "))*10**-2)
    chargeMagnitude[index] = (float(input("Input charge magnitude in nano Coulombs: "))*10**-9)
    index = index + 1

#Gets point of interest (POI)
def getPoint():
  pointYPosition = (float(input("Enter point of interest y position in centimeters: "))*10**-2)
  pointXPosition = (float(input("Enter point of interest x position in centimeters: "))*10**-2)
  return pointYPosition, pointXPosition

#Calculates the distance between each charge and the POI
def calcDist(pointY, pointX, amountCharges):
  for index in range(amountCharges):
    pointToChargeX[index] = pointX - chargeXPosition[index]
    pointToChargeY[index] = pointY - chargeYPosition[index]
    if pointToChargeX[index] == 0 and pointToChargeY[index] == 0:
      pointToCharge[index] = 0
    else:
      pointToCharge[index] = math.sqrt(pointToChargeX[index]**2+pointToChargeY[index]**2)
    


#Calculates the electric field at the POI due to each charge
def calcElectricField(amountCharges):
  for index in range(amountCharges):
    if pointToCharge[index] == 0:
      electricField[index] = 0
    else:
      electricField[index] = (k*chargeMagnitude[index])/pointToCharge[index]**2

#Calculates the angle from each charge to the POI
def calcAngle(amountCharges, pointY, pointX):
  for index in range(amountCharges):
    opp[index] = pointY - chargeYPosition[index]
    adj[index] = pointX - chargeXPosition[index]
    if opp[index] == 0 and adj[index] > 0:
      angleToPoint[index] = 0
    elif opp[index] == 0 and adj[index] < 0:
      angleToPoint[index] = math.pi
    elif adj[index] == 0 and opp[index] > 0:
      angleToPoint[index] = math.pi / 2
    elif adj[index] == 0 and opp[index] < 0:
      angleToPoint[index] = (3 * math.pi)/2
    else:
      if electricField[index] == 0:
        angleToPoint[index] = 0
      else:
        angleToPoint[index] = math.atan(abs(opp[index])/abs(adj[index]))
        if adj[index] < 0 and opp[index] > 0:
          angleToPoint[index] = angleToPoint[index] + (0.5 * math.pi)
        elif adj[index] < 0 and opp[index] < 0:
          angleToPoint[index] = angleToPoint[index] + (math.pi)
        elif adj[index] > 0 and opp[index] < 0:
          angleToPoint[index] = angleToPoint[index] + (1.5 * math.pi)
    angleToPoint[index] = math.degrees(angleToPoint[index])

#Calculates the x-component of the electric field from each charge to the POI
def calcXComponent(amountCharges, XTotal):
  for index in range(amountCharges):
    XComponent[index] = electricField[index] * math.cos(math.radians(angleToPoint[index]))
    XTotal = XTotal + XComponent[index]
  return XTotal

#Calculates the y-component of the electric field from each charge to the POI
def calcYComponent(amountCharges, YTotal):
  for index in range(amountCharges):
    YComponent[index] = electricField[index] * math.sin(math.radians(angleToPoint[index]))
    YTotal = YTotal + YComponent[index]
  return YTotal

#Calculates the straight line electric field force at the POI due to each charge
def finalCalc(YTotal, XTotal):
  YTotal = float(format(YTotal, '.2f'))
  XTotal = float(format(XTotal, '.2f'))
  electricFieldNet = math.sqrt(XTotal**2 + YTotal**2)
  if YTotal == 0 and XTotal > 0:
    angle = 0
  elif YTotal == 0 and XTotal < 0:
    angle = math.pi
  elif XTotal == 0 and YTotal > 0:
    angle = math.pi / 2
  elif XTotal == 0 and YTotal < 0:
    angle = (3 * math.pi) / 2
  elif XTotal == 0 and YTotal == 0:
    angle = 0
  else:
    angle = math.atan(YTotal / XTotal)
    if XTotal < 0 and YTotal > 0:
      angle = angle + (1 * math.pi)
    elif XTotal < 0 and YTotal < 0:
      angle = angle + math.pi
    elif XTotal > 0 and YTotal < 0:
      angle = angle + (1 * math.pi)
  angle = math.degrees(angle)
  return electricFieldNet, angle

#Finds the electric field at a random POI with the charges that the user input
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

#Finds the electric field at the POI the user input, but with random electric charges
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

#Prints the results from both random calculations
def outputRandom():
  index = 0
  while index < 5:
    print("Random charge " + str(index + 1) + " is at position (" + str(chargeXPosition[index]) + "," + str(chargeYPosition[index]) + ") with charge " + str(chargeMagnitude[index]))
    index += 1

#Outputs the final calculations
def output(electricFieldNet, angle, pointY, pointX):
  print("The electric field strength at (",pointX, ",",pointY,") is", format(electricFieldNet, ".2f"), "V/m." )
  print("The electric field angle is", format(angle, ".2f"), "degrees.")

main()