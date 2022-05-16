'''
COMP90024 Cluster and Cloud Computing Assignment 2
Team 22

Zizhao Li (1267416) zizhaol2@student.unimelb.edu.au (Suzhou, China)
Fu Zhu (1166186) fuzhu@student.unimelb.edu.au (Melbourne, Australia)
Chuting Wang (1074511) chutingw@student.unimelb.edu.au (Xi’an, China)
Xuezhu Wu (938808) xuezhuw@student.unimelb.edu.au (Hangzhou, China)
Yuepeng Sheng (1048382) yuepengs@student.unimelb.edu.au (Shanghai, China)
'''

import json
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

# read Greater Melbourne LGA json file
Greater_Melbourne = json.load(open('Data/map.json'))["features"]

"""
Input: 2d-tuple for example (144.96075, -37.80658)
Output: String of LGA name (MELBOURNE) or None

The function return the corrdinates corresponding LGA name,
if not foundable return None.
"""
def find_lga(coordinates):
    for lga in Greater_Melbourne:
        for polygon in lga['geometry']['coordinates']:
            if Polygon(polygon[0]).contains(Point(coordinates)):
                return lga['properties']["vic_lga__3"]
    return None