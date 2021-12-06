import math
import random

#Sets all variables
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

def getAmountCharges():
  amountCharges = int(input("How many charges do you want to have (Max of 5)?"))
  while amountCharges <= 0:
    print("Please enter a value greater than 0")
    amountCharges = int(input("How many charges do you want to have (Max of 5)?"))
  return amountCharges

def getCharges(amountCharges):
  for index in range(amountCharges):
    chargeXPosition[index] = (float(input("Input charge x position in centimeters: "))*10**-2)
    chargeYPosition[index] = (float(input("Input charge y position in centimeters: "))*10**-2)
    chargeMagnitude[index] = (float(input("Input charge magnitude in nano Coulombs: "))*10**-9)
    index = index + 1

def getPoint():
  pointYPosition = (float(input("Enter point of interest y position in centimeters: "))*10**-2)
  pointXPosition = (float(input("Enter point of interest x position in centimeters: "))*10**-2)
  return pointYPosition, pointXPosition

def calcDist(pointY, pointX, amountCharges):
  for index in range(amountCharges):
    pointToChargeX[index] = pointX - chargeXPosition[index]
    pointToChargeY[index] = pointY - chargeYPosition[index]
    pointToCharge[index] = math.sqrt(pointToChargeX[index]**2+pointToChargeY[index]**2)

def calcElectricField(amountCharges):
  for index in range(amountCharges):
    electricField[index] = (k*chargeMagnitude[index])/pointToCharge[index]**2

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
      angleToPoint[index] = math.atan(abs(opp[index])/abs(adj[index]))
      if adj[index] < 0 and opp[index] > 0:
        angleToPoint[index] = angleToPoint[index] + (0.5 * math.pi)
      elif adj[index] < 0 and opp[index] < 0:
        angleToPoint[index] = angleToPoint[index] + (math.pi)
      elif adj[index] > 0 and opp[index] < 0:
        angleToPoint[index] = angleToPoint[index] + (1.5 * math.pi)
    angleToPoint[index] = math.degrees(angleToPoint[index])

def calcXComponent(amountCharges, XTotal):
  for index in range(amountCharges):
    XComponent[index] = electricField[index] * math.cos(math.radians(angleToPoint[index]))
    XTotal = XTotal + XComponent[index]
  return XTotal

def calcYComponent(amountCharges, YTotal):
  for index in range(amountCharges):
    YComponent[index] = electricField[index] * math.sin(math.radians(angleToPoint[index]))
    YTotal = YTotal + YComponent[index]
  return YTotal

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

def findRandom():
  xRan = [0,0,0,0,0]
  yRan = [0,0,0,0,0]
  chargeRan = [0,0,0,0,0]
  for index in range(5):
    xRan[index] = random.random(-10,10)*10**2
    yRan[index] = random.random(-10,10)*10**2
    chargeRan[index] = random.random(-10,10)*10**2


def output(electricFieldNet, angle, pointY, pointX):
  print("The electric field strength at (",pointX, ",",pointY,") is", format(electricFieldNet, ".2f"), "V/m." )
  print("The electric field angle is", format(angle, ".2f"), "degrees.")

main()