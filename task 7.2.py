'''
Write a program to prompt for a file name, and then read through
the file and look for lines of the form:

X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
the line to extract the floating point number on the line. Count these lines and the
compute the total of the spam confidence values from these lines. When you reach
the end of the file, print out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519

Test your file on the mbox.txt and mbox-short.txt files.
'''

#fname = raw_input("Enter file name: ")
#fh = open("mbox.txt")
fh = open("mbox-short.txt")

count=0

summ=0

for line in fh:
    
    if not line.startswith("X-DSPAM-Confidence:") : continue

    count=count+1

    index=line.find('0')

    value=line [index:index+6]

    final_value=float(value)

    summ=summ+final_value
    
print 'Average spam confidence:',summ/count
