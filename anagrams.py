'''
Your task is to write a program which:

asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result.
Note:

assume that two empty strings are not anagrams;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check (treat them as non-existent)
'''

str_1 = input("Enter the first string: ")
str_2 = input("Enter the second string: ")

#remove spaces, change all letters to upper case, convert into list, sort the list, join list's elements into string
string_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
string_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
#compare both strings
if len(string_1) > 0 and string_1 == string_2:
	print("Anagrams")
else:
	print("Not anagrams")

'''
Test data:
Listen
Silent

modern
norman
'''