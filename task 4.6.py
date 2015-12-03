
'''
Rewrite your pay computation with time-and-a-half for overtime
and create a function called computepay which takes two parameters (hours and
rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''

import sys

def computepay(h,r):

    if (h<40) :

        pay=h*r

    elif (h>40) :

        pay=40*r+1.5*r*(h-40)
    
    return pay


hrs = raw_input("Enter Hours:")

rate = raw_input("Enter Hourly Rate:")

try:
        h = float(hrs)

        r = float(rate)

except:
        print "Please enter valid input"
        sys.exit(1)

p = computepay(h,r)

print "Pay:", p
