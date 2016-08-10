# -*- coding: utf-8 -*-
"""
ReadErsiShapefile.py
2016-08-10
Doug Charlton

This script takes in the location of an ERSI shapefile and converts is to a format that is more expediant to
plot on a cartesian plane.

Format is [[lat0,lon0],[lat1,lon1],...]
"""

import os,struct

SUFF_MAIN = '.shp' # the main file
SUF_INDX = '.shx'  # the index file
SUF_DBST = '.dbf'  # the dBASE Table

DIR = "C:\\Users\\dcharlto\\Documents\\GitHub\\MapPyData\\hshhg\\GSHHS_shp\\c";
FILE = "GSHHS_c_L3";

def ReadErsiRow(fObj,n_bytes,ret_type,is_big_endian):
    # read out the necessary number of bytes
    raw_bytes = fObj.read(n_bytes)

    # define the dictionary of strings for recasting the binary data
    castDic = {'int32':'1l','double':'1d'}
    cast_str = castDic[ret_type]
    if is_big_endian:
        cast_str = '!'+cast_str
        
    # recast the data and return it
    return struct.unpack(cast_str,raw_bytes)
    

# let's read in the main file
with open(os.path.join(DIR,FILE+SUFF_MAIN),'rb') as fObj:
    # read the file code
    file_code = ReadErsiRow(fObj,4,'int32',1)
    fObj.seek(24)
    file_length = ReadErsiRow(fObj,4,'int32',1)
    version = ReadErsiRow(fObj,4,'int32',0)
    shape_type = ReadErsiRow(fObj,4,'int32',0)
    x_min  = ReadErsiRow(fObj,8,'double',0)
    y_min  = ReadErsiRow(fObj,8,'double',0)
    x_max  = ReadErsiRow(fObj,8,'double',0)
    y_max  = ReadErsiRow(fObj,8,'double',0)
    z_min  = ReadErsiRow(fObj,8,'double',0)
    z_max  = ReadErsiRow(fObj,8,'double',0)
    m_min  = ReadErsiRow(fObj,8,'double',0)
    m_max  = ReadErsiRow(fObj,8,'double',0)
    
    

fObj.close()