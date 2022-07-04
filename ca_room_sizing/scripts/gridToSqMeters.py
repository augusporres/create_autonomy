#!/usr/bin/env python


import rospy
import numpy as np
from nav_msgs.msg import OccupancyGrid
import matplotlib.pyplot as plt
import sys

def squareMeters():
    file1=sys.argv[1] + '.pgm'
    file2=sys.argv[1] + '.yaml'
    f = open(file1, 'rb')
    f2 = open(file2, 'r')
    f2.readline() # reads first line
    resolution_field = f2.readline() #resolution is in 2nd line
    resolution = resolution_field.split()[1]
    print("Resolution", resolution)
    header = f.readline()
    f.readline() #author information
    (width, height) = [int(i) for i in f.readline().split()]
    depth = int(f.readline())
    assert depth <= 255
    raster = []
    for y in range(height):
        row = []
        for y in range(width):
            row.append(ord(f.read(1)))
        raster.append(row)
    f.close()
    raster = np.array(raster)
    binary_grid = toBinaryMatrix(raster)
    count = 0
    for x in range(0,len(binary_grid[:,0])):
        for y in range(0,len(binary_grid[0,:])):
            if (binary_grid[x,y] == 1): # if probability > 205 set to 1, else 0
                count +=1
    __height = np.array([0]*len(binary_grid[:,0]))
    __width = np.array([0]*len(binary_grid[0,:]))
    for y in range(0, len(binary_grid[:,0])):
        for x in range(0, len(binary_grid[0,:])):
            if binary_grid[y,x] == 1:
                __width[y] += 1
    for x in range(0, len(binary_grid[0,:])):
        for y in range(0, len(binary_grid[:,0])):
            if binary_grid[x,y] == 1:
                __height[y] += 1
    m2 = __height.max() * __width.max() * float(resolution)**2
    print("Ancho de celdas ocupadas: ", __width.max())
    print("Alto de celdas ocupadas: ", __height.max())
    print("Metros cuadrados: ", m2)

def toBinaryMatrix(data):
    filtro = data[data[:,:] > 205]
    for x in range(0,len(data[:,0])):
        for y in range(0,len(data[0,:])):
            if (data[x,y] > 205): # if probability > 205 set to 1, else 0
                data[x,y] = 1
            else:
                data[x,y] = 0
    print("OcGrid transformed succesfully to binary")
    return data
    

if __name__=='__main__':
    squareMeters()