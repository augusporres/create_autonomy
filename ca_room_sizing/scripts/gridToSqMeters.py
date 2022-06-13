#!/usr/bin/env python


import rospy
import numpy as np
from nav_msgs.msg import OccupancyGrid
import matplotlib.pyplot as plt


def squareMeters():
    #f = open('corridor_mapping_augusto.pgm', 'rb')
    with open('corridor_mapping_augusto.pgm', 'rb') as f:
        im = plt.imread(f)
    plt.plot(im)
    #print(f.readline())
    #print(f.readline())
    """(width, height) = [int(i) for i in f.readline().split()]
    depth = int(f.readline())
    raster = []
    for y in range(height):
        row = []
        for y in range(width):
            row.append(ord(f.read(1)))
        raster.append(row)
    raster = np.array(raster)
    toBinaryMatrix(raster)"""
    f.close()

def toBinaryMatrix(data):
    for x in range(0,len(data)):
        for y in range(0,len(data)):
            if (data[x][y] > 50): # if probability > 50 set to 1, else 0
                data[x][y] = 1
            else:
                data[x][y] = 0
    print(data)
    

if __name__=='__main__':
    squareMeters()