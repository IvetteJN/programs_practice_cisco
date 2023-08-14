'''
This cipher was (probably) invented and used by Gaius Julius Caesar and his troops during the Gallic Wars. 
The idea is rather simple – every letter of the message is replaced by its nearest consequent (A becomes B, B becomes C, and so on). 
The only exception is Z, which becomes A.
*it accepts Latin letters only (note: the Romans didn't use whitespaces or digits)
*all letters of the message are in upper case (note: the Romans knew only capitals)
'''


#ask the user to enter the open (unencrypted), one-line message
text = input("Enter your message: ")
#prepare a string for an encrypted message (empty for now)
cipher = ''
#start the iteration through the message
for char in text:
    #if the current character is not alphabetic
    if not char.isalpha():
        #ignore it
        continue
    #convert the letter to upper-case (it's preferable to do it blindly, rather than check whether it's needed or not)
    char = char.upper()
    #get the code of the letter and increment it by one;
    code = ord(char) + 1
    #if the resulting code has "left" the Latin alphabet (if it's greater than the Z code)
    if code > ord('Z'):
        #change it to the A code;
        code = ord('A')
    #append the received character to the end of the encrypted message
    cipher += chr(code)

print(cipher)

'''Improving the Caesar's Cipher:
Your task is to write a program which:

*asks the user for one line of text to encrypt;
*asks the user for a shift value (an integer number from the range 1..25 - note: you should force 
the user to enter a valid shift value (don't give up and don't let bad data fool you!)
*prints out the encoded text.
'''

# Enter a valid shift value (repeat until it succeeds).
shift = 0

while shift == 0:
    try:    
        shift = int(input("Enter the cipher shift value (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Incorrect shift value!")

cipher = ''

for char in text:
    # Is it a letter?
    if char.isalpha():
        # Shift its code.
        code = ord(char) + shift
        # Find the code of the first letter (upper- or lower-case)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # Make correction.
        code -= first
        code %= 26
        # Append the encoded character to the message.
        cipher += chr(first + code)
    else:
        # Append the original character to the message.
        cipher += char

print(cipher)
