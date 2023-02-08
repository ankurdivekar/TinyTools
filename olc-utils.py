import os
import pandas as pd
from openlocationcode import openlocationcode as olc

def get_offset_gridchar(start, offset):
    gridseq = ["2","3","4","5","6","7","8","9","C","F","G","H","J","M","P","Q","R","V","W","X"]
    if start not in gridseq:
        return None
    else:
        start_idx = gridseq.index(start)
        wraparounds = int((offset/abs(offset))*(abs(offset) // len(gridseq)))
        local_offset = int((offset/abs(offset))*(abs(offset) % len(gridseq)))
        
        # print(start_idx, wraparounds, local_offset)
        
        if start_idx + local_offset < 0:
            return gridseq[start_idx + local_offset + len(gridseq)], wraparounds-1
        
        elif start_idx + local_offset > len(gridseq)-1:
            return gridseq[start_idx + local_offset - len(gridseq)], wraparounds+1
        
        else:
            return gridseq[start_idx + local_offset], wraparounds
    
get_offset_gridchar('C', -43)

def get_olc_with_offsets(olc_code, v_offset=0, h_offset=0):
    if olc_code is None:
        return None
    else:
        # Split the OLC code into its component parts.
        olc_code = ''.join(olc_code.split("+"))
        olc_components = [olc_code[i:i+2] for i in range(0, len(olc_code), 2)]
        # print(olc_components)
        
        component_pointer = len(olc_components)
        wraparound = True
        
        while wraparound:
            component_pointer -= 1
            component = olc_components[component_pointer]
            v_char = component[0]
            h_char = component[1]
            
            if v_offset != 0:
                v_char, v_offset = get_offset_gridchar(component[0], v_offset)
            if h_offset != 0:
                h_char, h_offset = get_offset_gridchar(component[1], h_offset)
            
            new_component = v_char + h_char
            olc_components[component_pointer] = new_component
            wraparound = v_offset != 0 or h_offset != 0
        
        if len(olc_components) > 4:
            olc_code = ''.join(olc_components[:4]) + '+' + ''.join(olc_components[4:])
        else:
            olc_code = ''.join(olc_components)
            
        return olc_code
        
# get_olc_with_offsets('7JCMHQ9C+2W', -430, -2)
get_olc_with_offsets('84VVHQMX', -1, -1)

def get_olc_8_neighbours(olc_code):
    
    if olc_code is None:
        return None
    else:
        NW = get_olc_with_offsets(olc_code, 1, -1)
        N = get_olc_with_offsets(olc_code, 1, 0)
        NE = get_olc_with_offsets(olc_code, 1, 1)
        E = get_olc_with_offsets(olc_code, 0, 1)
        SE = get_olc_with_offsets(olc_code, -1, 1)
        S = get_olc_with_offsets(olc_code, -1, 0)
        SW = get_olc_with_offsets(olc_code, -1, -1)
        W = get_olc_with_offsets(olc_code, 0, -1)
        
        # neighbours = []
        
        # return ','.join([NW, N, NE, E, SE, S, SW, W])
        return NW, N, NE, E, SE, S, SW, W

get_olc_8_neighbours(olc_code='7JCMHQ9C')

def get_old_grid_centroid(olc_code):
    if olc_code is None:
        return None
    else:
        if not olc_code.endswith("+"):
            olc_code = olc_code + "+"
            g = olc.decode(olc_code)
            return g.latitudeCenter, g.longitudeCenter

get_old_grid_centroid('84VVHQMX')        
