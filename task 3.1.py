
'''
Write your pay computation to give the employee 1.5 times the
hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''

hrs = raw_input("Enter Hours:")
h = float(hrs)

rate = raw_input("Enter Hourly Rate:")
r = float(rate)

if (h<40) :

    pay=h*r

    print "Pay:", pay

elif (h>40) :

    pay=40*r+1.5*r*(h-40)

    print "Pay:", pay
