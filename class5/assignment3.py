'''
Exercise - Valid email
Write some code that takes input from the user and prints whether it's a valid email address. Make sure to sanitize the user input with .strip()
An email address is valid if:
It has a "." at the third-to-last index
It has exactly one "@" symbol, at the fifth-to-last index or earlier
There is at least one character before the "@" symbol
It doesn't have any spaces (doesn't contain " ")
If all these conditions are met, print True. Otherwise, print False.
To do this, use boolean statements on your string.
Test your code on a few inputs to make sure it works!

'''

# Get input 
email = input("Hello, please enter your email: ")


# Clean data
email = email.strip() # cleaning the string with strip method





# Test 1: It has a "." at the third-to-last index
test_1 = (email[-4] == '.')
print(f'Test 1: Does {email} have a "." at the third-to-last index? ', test_1)

# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier
test_2 = ('@' in email[-5::-1]) # use "in" keyword for true/false(Boolean)
print(f'Test 2: Does {email} have exactly one "@" symbol, at the fifth-to-last index or earlier?',test_2)


# Test 3: There is at least one character before the "@" symbol
'''test_3 = (email[0] != '@')#test if the first character is not equal to at "!" is not
'''
test_3 = (email.index('@') > 0)# another solution
print(f'Test 3: There is at least one character before the "@" symbol in {email}', test_3)

# Test 4: It doesn’t have any spaces (doesn’t contain " ")

# Final Test with AND Keyword
