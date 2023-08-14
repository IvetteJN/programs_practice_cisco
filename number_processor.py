'''This program shows a simple method allowing you to input a line filled with numbers, and to process them easily. 
Note: the routine input() function, combined together with the int() or float() functions, is unsuitable for this purpose.
'''
#ask the user to enter a line filled with any number of numbers (the numbers can be floats)
line = input("Enter a line of numbers - separate them with spaces: ")
#split the line receiving a list of substrings
strings = line.split()
#initiate the total sum to zero
total = 0
#as the string-float conversion may raise an exception, it's best to continue by using the try-except block
try:
    #iterate through the list
    for substr in strings:
        #and try to convert all its elements into float numbers; if it works, increase the sum
        total += float(substr)
    print("The total is:", total)
#the program ends here in the case of an error
except:
    #print a diagnostic message showing the user the reason for the failure
    print(substr, "is not a number.")