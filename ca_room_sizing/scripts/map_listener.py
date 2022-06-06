#!/usr/bin/env python


import rospy
import numpy as np
from nav_msgs.msg import OccupancyGrid

def callback(data):
    rospy.loginfo("\nHeader: \n%s",data.header)
    rospy.loginfo("\nMetadata: \n%s",data.info)
    toBinaryMatrix(data.data)
    #rospy.loginfo("Data: %s",data.data)

def toBinaryMatrix(data):
    data = list(data)
    for i in range(0,len(data)):
        if (data[i] > 50): # if probability > 50 set to 1, else 0
            data[i] = 1
        else:
            data[i] = 0
    f = open('map_data', 'w')
    for item in data:
        f.write("%s, " %item)  
    f.close() 
    

def listener():
    rospy.init_node('map_listener', anonymous=True)
    rate = rospy.Rate(0.2)# Correr callback cada 5segs
    rospy.Subscriber('map', OccupancyGrid, callback) # or nav_msgs.OccupancyGrid
    rate.sleep()
    rospy.spin()

if __name__=='__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass