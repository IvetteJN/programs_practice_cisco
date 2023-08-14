'''This program implements an algorithm used by European banks to specify account numbers. 
The standard named IBAN (International Bank Account Number) provides a simple and fairly reliable 
method for validating account numbers against simple typos that can occur during rewriting of the number, 
for example, from paper documents, like invoices or bills, into computers.

An IBAN-compliant account number consists of:

*a two-letter country code taken from the ISO 3166-1 standard (e.g., FR for France, GB for Great Britain, DE for Germany, and so on)
*two check digits used to perform the validity checks (fast and simple, but not fully reliable, tests, showing whether a number is 
invalid (distorted by a typo) or seems to be good);
*the actual account number (up to 30 alphanumeric characters (the length of that part depends on the country))
*The standard says that validation requires the following steps (according to Wikipedia):

(step 1) Check that the total IBAN length is correct as per the country (this program won't do that, but you can modify 
the code to meet this requirement if you wish; note: you have to teach the code all the lengths used in Europe)
(step 2) Move the four initial characters to the end of the string (i.e., the country code and the check digits)
(step 3) Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11 ... Z = 35;
(step 4) Interpret the string as a decimal integer and compute the remainder of that number by modulo-dividing it by 97; 
If the remainder is 1, the check digit test is passed and the IBAN might be valid.
'''

#ask the user to enter the IBAN (the number can contain spaces, as they significantly improve number readability
iban = input("Enter IBAN, please: ")
#but remove them immediately
iban = iban.replace(' ','')

#the entered IBAN must consist of digits and letters only – if it doesn't
if not iban.isalnum():
    #output the message
    print("You have entered invalid characters.")
#the IBAN mustn't be shorter than 15 characters (this is the shortest variant, used in Norway)
elif len(iban) < 15:
    #if it is shorter, the user is informed;
    print("IBAN entered is too short.")
#the IBAN cannot be longer than 31 characters (this is the longest variant, used in Malta)
elif len(iban) > 31:
    print("IBAN entered is too long.")
#move the four initial characters to the number's end, and convert all letters to upper case (step 02 of the algorithm)
else:
    iban = (iban[4:] + iban[0:4]).upper()
    #this is the variable used to complete the number, created by replacing the letters with digits (according to the algorithm's step 03)
    iban2 = ''
    #iterate
    for ch in iban:
        #if the character is a digit
        if ch.isdigit():
            #just copy it
            iban2 += ch
        else:
            #convert it into two digits
            iban2 += str(10 + ord(ch) - ord('A'))
    #the converted form of the IBAN is ready – make an integer out of it     
    iban = int(iban2)
    #is the remainder of the division of iban2 by 97 equal to 1
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")

'''
Test data:
British: GB72 HBZU 7006 7212 1253 00
French: FR76 30003 03620 00020216907 50
German: DE02100100100152517108
'''