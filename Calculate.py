import string
from numpy import *

#points in the 3rd and 4th quadrant will have a negative polar angle
#positiveTheta fixes that by adding 2pi if it is negative before adding any optional rotation
positiveTheta = True
#decimal places to round to
dec = 6
#each point will have an added rot 1 more than the last
spinnymode = False

testPoints = [(-10, 7),(-8, 6,10),(-5, -5),(6, -4),(-4, 6)]


CPoints = []
#set this to False to not read from Settings.txt
if True:
    settings = open("Settings.txt")
    
    [settings.readline() for i in range(3)] #skip first 3 lines
    if('T' in settings.readline().upper()):
        positiveTheta = True
        
    settings.readline() #skip line
    dec = int(settings.readline().strip())
    
    settings.readline() #skip line
    if('T' in settings.readline().upper()):
        spinnymode = True

    settings.readline()
    pts = []
    
    for line in settings:
        state = 0 #0 = out of point; 1 = in point
        temp = ""
        for chr in line:
            if(state == 0):
                if(chr == '('):
                    state = 1
            elif(state == 1):
                if(chr == ')'):
                    pts.append(temp.split(","))
                    state = 0
                    temp = ""
                else:
                    temp+=chr
                    
    #turns string vals into float
    cPoints = [[float(val.strip()) for val in pt] for pt in pts] 
    settings.close()
else:
    CPoints = testPoints
                    



#see below methods for file writing

def C2P(point):
    #converts (x,y,[rot = 0]) to (r,theta+rot*2pi)
    x = point[0]
    y = point[1]
    r = (x**2+y**2)**.5
    theta = arctan2(y,x)
    #makes theta positive if positiveTheta is true
    if(theta < 0 and positiveTheta):
        theta += 2*pi
    rot = 0
    # adds optional rotation
    if(len(point) > 2):
        rot = point[2]
    return (r, theta+rot*2*pi)
def cars2Pols(cPoints):
    #calls C2P to turn a list of cartesian points into polar
    lis = [C2P(x) for x in cPoints]
    if(spinnymode):
        lis = [(lis[i][0],lis[i][1]+2*pi*i) for i in range(len(lis))]
    return lis

def carCalcLine(cPoints):
    #creates and solves the martix for interpolation in cartesian (x,y)
    A = [[point[0]**pow for pow in range(len(cPoints))] for point in cPoints]
    b = [point[1] for point in cPoints]
    return linalg.solve(A,b)
def carFindLine(cPoints):
    #calls and returns the rref as an equasion cartesian (x,y)
    lis = carCalcLine(cPoints)
    #y = a1 + a2x + a3x^2 +...
    out = "y = " + str(round(lis[0],dec))
    for i in range(1,len(lis)):
        out += " + " + str(round(lis[i],dec)) + "*x^" + str(i)
    return out


def polCalcLine(pPoints):
    #creates and solves the martix for interpolation in polar (r,theta)
    A = [[point[1]**pow for pow in range(len(pPoints))] for point in pPoints]
    b = [point[0] for point in pPoints]
    return linalg.solve(A,b)
def polFindLine(pPoints):
    #calls and returns the rref as an equasion polar (r,theta)
    lis = polCalcLine(pPoints)
    #r = a1 + a2θ + a3θ^2 +...
    out = "r = " + str(round(lis[0],dec))
    for i in range(1,len(lis)):
        out += " + " + str(round(lis[i],dec)) + "*\\theta^" + str(i)
    return out

#file writing. change to false to not write
if True:
    output = open("Output.txt", "w")
    
    output.write("Cartesian Coordinates:\n")
    for i in cPoints:
        output.write( "(" + str(round(i[0], dec)) + ", " +
                     str(round(i[1], dec)) + ")" )
        if(i != cPoints[len(cPoints)-1]):
            output.write(", ")
    
    
    
    pPoints = cars2Pols(cPoints)
    
    output.write("\nPolar Coordinates:\n")
    for i in pPoints:
        output.write( "(" + str(round(i[0], dec)) + ", " +
                     str(round(i[1], dec)) + ")" )
        if(i != pPoints[len(pPoints)-1]):
            output.write(", ")
    
    
    
    carFindLine(cPoints)
    output.write("\n\nCartesian Equasion:\n")
    try:
        output.write(carFindLine(cPoints))
    except BaseException as err:
        output.write("Error Occurred: " + str(err))
    
    
    output.write("\nPolar Equasion:\n")
    try:
        output.write(polFindLine(pPoints))
    except BaseException as err:
        output.write("Error Occurred: " + str(err))
    output.close()
        
if False:
    pPoints = cars2Pols(cPoints)
    print(cPoints)
    print(pPoints)
    carFindLine(cPoints)
    polFindLine(pPoints)