#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from vectornav.msg import Ins
from std_msgs.msg import Float32MultiArray

pub = rospy.Publisher('/imu_INS',Float32MultiArray, queue_size=10)
msg = Ins()
msg2 = Float32MultiArray()
is_first_sub=0

def callback(data):
    global msg,is_first_sub
    msg = data
    is_first_sub=1

if __name__ == '__main__':
    try:
        rospy.init_node('custom_listener', anonymous=True) #Se crea el Nodo
        rospy.Subscriber("vectornav/INS", Ins, callback)
        rate = rospy.Rate(100) #100 hz
        while not rospy.is_shutdown():
            
            if is_first_sub:
                msg2.data=[msg.nedVelX,msg.nedVelY]
                pub.publish(msg2)
                print(msg2.data)
                rate.sleep() #Espera para cumplir el rate
    except rospy.ROSInterruptException:
        pass
