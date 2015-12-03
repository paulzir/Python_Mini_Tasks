'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
Note that the autograder does not have support for the sorted() function.
'''

fname = "mbox-short.txt"

handle = open(fname)

lst=list()

hours=list()

counts=dict()

for line in handle :

    line=line.rstrip()

    if line.startswith('From '):

        words=line.split()

        lst.append(words[5])

for time in lst :

    time=time.split(':')

    hours.append(time[0])

for hour in hours:

   counts[hour]=counts.get(hour,0)+1

newlst=list()

for key,val in counts.items():

    newlst.append((key,val))

newlst.sort()

for key,val in newlst:

    print key, val