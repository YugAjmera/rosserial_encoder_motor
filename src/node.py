#!/usr/bin/env python

import rospy
from rosserial_encoder_motor.msg import motor

rospy.init_node('cmd_Publisher')
pub = rospy.Publisher('/control_motor', motor, queue_size=1)

rate=rospy.Rate(2)

vel = motor()

vel.direction=70
vel.speed=100
vel.name=3

pub.publish(vel)
