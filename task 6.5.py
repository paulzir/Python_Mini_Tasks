
'''
Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence: 0.8475'

Use find and string slicing to extract the portion of the string after the colon
character and then use the float function to convert the extracted string into a
floating point number.
'''

text = "X-DSPAM-Confidence: 0.8475";

index=text.find('0')

value=text[index:index+6]

final_value=float(value)

print final_value
