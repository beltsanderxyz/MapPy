# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:51:55 2016

@author: Doug Charlton
"""
import struct

def readErsiRow(fObj,ret_type,n_vals=1,is_big_endian=0):
    
       
    # read out the necessary number of bytes

    # define the dictionary of strings for recasting the binary data
    # format is [def_type,n_bytes_per_value]
    castDic = {'int32':('l',4),'double':('d',8)}
    typeTup = castDic[ret_type]
    raw_bytes = fObj.read(n_vals*typeTup[1])

    cast_str = "%d%s" % (n_vals,typeTup[0])
    if is_big_endian:
        cast_str = '!'+cast_str
        
    # recast the data and return it
    unpacked_data = struct.unpack(cast_str,raw_bytes)
    if n_vals == 1:
        unpacked_data = unpacked_data[0]
    return unpacked_data
    
    
def readShapePolygon(fObj):
    # reads a single Polygon shapetype. See official ERSI documentation for definition
    
    shape_type  = readErsiRow(fObj,'int32')
    assert shape_type==5, "shapetype mismatch. Expected 5, found %d" % shape_type
    
    bounding_box  = readErsiRow(fObj,'double',4)
    n_parts  = readErsiRow(fObj,'int32')
    n_pts  = readErsiRow(fObj,'int32')
    
    parts =  readErsiRow(fObj,'int32',n_parts)  
    
    # for each collection of parts, read in the points
    if n_parts == 1:
        points = [readErsiRow(fObj,'double',2*n_pts)]
    else:
        ix_stop  = n_parts[2:n_parts]
        ix_stop.append(n_pts)
        points = []
        
        # read in the points for each part
        for ii in range(1,n_parts):
            n_pts_to_read = 1+ix_stop[ii]-parts[ii]
            points_temp = readErsiRow(fObj,'double',2*n_pts_to_read)
            points.append(points_temp)
    

    return [bounding_box,n_parts,n_pts,parts,points]

def readShapePoint(fObj,n_pts=1,read_shape_type=1):
    # reads out one or more Point shapetypes
    

    readErsiRow(fObj,)