#!/usr/bin/env python

from __future__ import print_function

import rospy

from rosserial_encoder_motor.msg import motor

import sys, select, termios, tty

msg = """
Reading from the keyboard !
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >


anything else : stop

q/z : increase/decrease max speeds by 10%

CTRL-C to quit
"""

moveBindings = {
        'i':(-1,0,1),
        'o':(-1,1,0),
        'j':(1,1,1),
        'l':(-1,-1,-1),
        'u':(-1,0,1),
        ',':(1,0,-1),
        '.':(0,1,-1),
        'm':(1,-1,0),  
        'O':(-1,1,0),
        'I':(-1,0,1),
        'J':(1,-2,1),
        'L':(-1,2,-1),
        'U':(0,-1,1),
        '<':(1,0,-1),
        '>':(0,1,-1),
        'M':(1,-1,0),  
    }

speedBindings={
        'q':(1.1,1.1),
        'z':(.9,.9),
    }

def getKey():
    tty.setraw(sys.stdin.fileno())
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def vels(speed):
    return "currently:\tspeed %s " % (speed)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('vel_Publisher')
    publ = rospy.Publisher('/control_motor', motor, queue_size=1)
    pubb = rospy.Publisher('/control_motor', motor, queue_size=1)
    pubr = rospy.Publisher('/control_motor', motor, queue_size=1)


    speed = 100
    x = 0
    y = 0
    z = 0
    status = 0
    rate=rospy.Rate(2)

    print(msg)
    print(vels(speed))
    while(1):
            key = getKey()
            if key in moveBindings.keys():
                x = moveBindings[key][0]
                y = moveBindings[key][1]
                z = moveBindings[key][2]
            elif key in speedBindings.keys():
                speed = speed * speedBindings[key][0]
       
                print(vels(speed))
                if (status == 14):
                    print(msg)
                status = (status + 1) % 15
            else:
                x = 0
                y = 0
                z = 0
                th = 0
                if (key == '\x03'):
                    break

            vell = motor()

	    if (x>=0):	
		vell.direction = 70
	    if (x<0): 	
		vell.direction = 66
		x=-x 
	    vell.speed = speed*x
            vell.name=2
	
	    velb = motor()

	    if (y>=0):	
		velb.direction=70
	    if (y<0): 	
		velb.direction=66
		y=-y 
	    velb.speed=speed*y
            velb.name=3
	
	    velr = motor()

	    if (z>=0):	
		velr.direction=70
	    if (z<0): 	
		velr.direction=66
		z=-z 
	    velr.speed=speed*z
            velr.name=1
		
	    print (vell)
	    print(velb)
            print(velr)
	

	    publ.publish(vell)
	    pubb.publish(velb)
	    pubr.publish(velr)

