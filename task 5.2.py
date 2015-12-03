
'''
Write another program that prompts for a list of numbers as above and at the
end prints out both the maximum and minimum of the numbers instead of the
average.
'''

largest = None
smallest = None

while True:

    number = raw_input("Enter a number: ")

    if number == "done" :
            break

    try:
    
        num=int(number)
    
        if smallest is None or num<smallest:
            smallest=num

        if largest is None or num>largest:
            largest=num

    except:

        print "Invalid input"

print "Maximum is", largest

print "Minimum is", smallest

    
