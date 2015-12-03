'''
Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

fname = "mbox-short.txt"

fh = open(fname)

count = 0

lst=list()

counts=dict()

for line in fh :

    line=line.rstrip()

    if line.startswith('From'):

        words=line.split()

        if len(words[0])<5:

            lst.append(words[1])

for word in lst:

   counts[word]=counts.get(word,0)+1

maximum = None
mail = None

for key,count in counts.items():

    if maximum is None or count>maximum :

        maximum=count
        mail=key

print mail, maximum
