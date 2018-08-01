#############################################################
#    MIT License                                            #
#    Copyright (c) 2018 Omiya-Giken LLC                     #
#############################################################
# -*- coding: utf-8 -*-
from __future__ import print_function
from PyMCP2221A import PyMCP2221A

import time

gI2c_address = 0x77
gDigT = []
gDigP = []
gDigH = []
gT_fine = 0.0


def setup():
    print('-'*50)
    print('MCP2221(A) with BME280 ')
    print('-'*50)
#    gMcp2221 = PyMCP2221A.PyMCP2221A()
    gMcp2221.Reset()
#    gMcp2221 = PyMCP2221A.PyMCP2221A()

    gMcp2221.I2C_Init()


def get_calib_param():
    calib = []
    calib.append(gMcp2221.I2C_Read(gI2c_address,0x88))
    calib.append(gMcp2221.I2C_Read(gI2c_address,0x89))
    calib.append(gMcp2221.I2C_Read(gI2c_address,0x8a))

    time.sleep(10)
    calib.append(gMcp2221.I2C_Read(gI2c_address,0x8b))
    calib.append(gMcp2221.I2C_Read(gI2c_address,0x8c))
    calib.append(gMcp2221.I2C_Read(gI2c_address,0x8d))

    time.sleep(10)
    calib.append(gMcp2221.I2C_Read(gI2c_address,0x8e))
    calib.append(gMcp2221.I2C_Read(gI2c_address,0x8f))
    calib.append(gMcp2221.I2C_Read(gI2c_address,0x90))
    time.sleep(10)
    calib.append(gMcp2221.I2C_Read(gI2c_address,0x91))
    calib.append(gMcp2221.I2C_Read(gI2c_address,0x92))
    calib.append(gMcp2221.I2C_Read(gI2c_address,0x93))

'''
#    for i in range (0x88,0x88+24):
    for i in range (0x88,0x88+2):
#        calib.append(gMcp2221.I2C_Read(gI2c_address,i))
        temporay = gMcp2221.I2C_Read(gI2c_address,i)
        print("Getting data")
        calib.append(temporay)
    for i in range (0x8a,0x8a+2):
        calib.append(gMcp2221.I2C_Read(gI2c_address,i))
        temporay = gMcp2221.I2C_Read(gI2c_address,i)
#        print("Getting data")
        calib.append(temporay)

    calib.append(gMcp2221.I2C_Read(gI2c_address,0xA1))
    for i in range (0xE1,0xE1+7):
        calib.append(gMcp2221.I2C_Read(gI2c_address,i))
    gDigT.append((calib[1] << 8) | calib[0])
    gDigT.append((calib[3] << 8) | calib[2])
    gDigT.append((calib[5] << 8) | calib[4])

    gDigP.append((calib[7] << 8) | calib[6])
    gDigP.append((calib[9] << 8) | calib[8])
    gDigP.append((calib[11]<< 8) | calib[10])
    gDigP.append((calib[13]<< 8) | calib[12])
    gDigP.append((calib[15]<< 8) | calib[14])
    gDigP.append((calib[17]<< 8) | calib[16])
    gDigP.append((calib[19]<< 8) | calib[18])
    gDigP.append((calib[21]<< 8) | calib[20])
    gDigP.append((calib[23]<< 8) | calib[22])

    gDigH.append( calib[24] )
    gDigH.append((calib[26]<< 8) | calib[25])
    gDigH.append( calib[27] )
    gDigH.append((calib[28]<< 4) | (0x0F & calib[29]))
    gDigH.append((calib[30]<< 4) | ((calib[29] >> 4) & 0x0F))
    gDigH.append( calib[31] )
    
    for i in range(1,2):
        if gDigT[i] & 0x8000:
            gDigT[i] = (- gDigT[i] ^ 0xFFFF) + 1
    for i in range(1,8):
        if gDigP[i] & 0x8000:
            gDigP[i] = (- gDigP[i] ^ 0xFFFF) + 1
    for i in range(0,6):
        if gDigH[i] & 0x8000:
            gDigH[i] = (-gDigH[i] ^ 0xFFFF) + 1  
'''

if __name__ == '__main__':
    print('-'*50)
    print('MCP2221(A) with BME280 ')
    print('-'*50)
    gMcp2221 = PyMCP2221A.PyMCP2221A()
    gMcp2221.Reset()
    gMcp2221 = PyMCP2221A.PyMCP2221A()
    gMcp2221.I2C_Init()

    get_calib_param()
