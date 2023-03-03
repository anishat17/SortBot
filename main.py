# Main loop here
import threading
import CameraInput
import RobotFunctions
import RobotAPI
import time

t = None
t1 = None
def turnright( degrees):
    global t
    RobotAPI.turnRight(int(degrees))
    t= None   
def turnleft( degrees):
    global t
    RobotAPI.turnLeft(int(degrees))
    t= None
def lowercrane( ):
    global t
    print("lowercrane")
    RobotAPI.lowerCrane()
    t= None
    



margin =50
turnAngle= 45

print("Running main.py")

CameraInput.testprint()
RobotAPI.returnCraneToCenter()
time.sleep(2)
y = 0
initiateCamera = True
centerX, centerY = CameraInput.getCameraCenterCoordinate()
#for i in CameraInput.trackFace():
#    print(i, ";", centerX, end=' ')
#    if (i[0] >= centerX):
#        print("Camera looking too far left! Must turn towards right...")
#        #RobotAPI.indicateTurnLeft()
#    else:
#        print("Camera looking too far right! Must turn towards left...")
#        #RobotAPI.indicateTurnRight()


for i in CameraInput.trackObject():

    if (initiateCamera):
        time.sleep(1)
        initiateCamera = False
    if (t == None):
        print(i, ";", centerX, end=' ')
        if ( y <= 20 ):
            y+=1
        else:
            y = 1
            time.sleep(2)
            print ("reset")
            RobotAPI.returnCraneToCenter()
        if (i[0] < centerX-margin):
            degree= turnAngle/y
            print(degree, "left")
#             RobotAPI.indicateTurnLeft()
            t = threading.Thread(target= turnleft, args=(degree,))
            t.start()
#             RobotAPI.turnLeft(int(degree))
            
        elif(i[0] > centerX+margin):
            degree= turnAngle/y
            print(degree, "right")
#             RobotAPI.indicateTurnRight()
#             RobotAPI.turnRight(int(degree))
            t = threading.Thread(target= turnright, args=(degree,))
            t.start()
            time.sleep(2)
        else:
            print("centered")
            t = threading.Thread(target= lowercrane)
            t.start()
#             RobotAPI.lowerCrane()
            time.sleep(3)
            #RobotAPI.turnOnMagnet()
            #time.sleep(1)
#             RobotAPI.returnCraneToCenter()
            time.sleep(5)
            y=0
        
        
        
        

    
