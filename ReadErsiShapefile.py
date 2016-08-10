# -*- coding: utf-8 -*-
"""
ReadErsiShapefile.py
2016-08-10
Doug Charlton

This script takes in the location of an ERSI shapefile and converts is to a format that is more expediant to
plot on a cartesian plane.

Format is [[lat0,lon0],[lat1,lon1],...]
"""

import os
import ersiParseFuncs as ersi

SUFF_MAIN = '.shp' # the main file
SUF_INDX = '.shx'  # the index file
SUF_DBST = '.dbf'  # the dBASE Table

DIR = "C:\\Users\\dcharlto\\Documents\\GitHub\\MapPyData\\hshhg\\GSHHS_shp\\c";
FILE = "GSHHS_c_L3";

    

# let's read in the main file
with open(os.path.join(DIR,FILE+SUFF_MAIN),'rb') as fObj:
    # read the file code
    file_code = ersi.readErsiRow(fObj,'int32',1,1)
    fObj.seek(24)
    file_length = ersi.readErsiRow(fObj,'int32',1,1)
    version = ersi.readErsiRow(fObj,'int32')
    shape_type = ersi.readErsiRow(fObj,'int32')
    x_min  = ersi.readErsiRow(fObj,'double')
    y_min  = ersi.readErsiRow(fObj,'double')
    x_max  = ersi.readErsiRow(fObj,'double')
    y_max  = ersi.readErsiRow(fObj,'double')
    z_min  = ersi.readErsiRow(fObj,'double')
    z_max  = ersi.readErsiRow(fObj,'double')
    m_min  = ersi.readErsiRow(fObj,'double')
    m_max  = ersi.readErsiRow(fObj,'double')
    
    
    rec_num  = ersi.readErsiRow(fObj,'int32',1,1)
    rec_len  = ersi.readErsiRow(fObj,'int32',1,1)
    
    # TODO: implement all shapetypes
    
    if shape_type == 5:
        # the shapefile is of polygon type
        temp = ersi.readShapePolygon(fObj)
    

fObj.close()