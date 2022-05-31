"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input

07:05:45PM
Sample Output

19:05:45
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    s = s.upper()
    time_list = list(map(lambda a:int(a),s[:-2].split(":")))
    is_pm = s[-2:] == "PM"
    if is_pm:
        if time_list[0] == 12:
            time_list[0] = 12
        else:
            time_list[0] =12 + time_list[0] 
    else:
        if time_list[0] == 12:
            time_list[0] = 0
            
        
    return (":".join(list(map(lambda a : '{:02}'.format(a), time_list) )  ))
    
if __name__ == '__main__':
    s = "07:05:45PM"
    result = timeConversion(s)
    print(result)