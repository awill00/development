''' Exercise - Challenge

Write some code that will print a box around a string.

Examples:
User input: hello
*******
*hello*
*******

User input: programming is fun
********************
*programming is fun*
********************
Hint: You will have to use the len() function, string concatenation (+), and string multiplication (*)

'''


#Get user input
# userinput = input("What is you word or phrase? ")


#Create top and Bottom Border
# top_and_bottom_border = (len(userinput) * '*') + '**'


# Generate output
# print(top_and_bottom_border)
# print('*' + userinput + '*')
# print(top_and_bottom_border)


''' Strings Part 2'''

# Strings are immutable
# just applying method to the string won't change original value
str_1 = 'BLUE' 
str_1.lower()

str_1 = str_1.lower()# have to assign it for it to take effect
#print(str_1)

''''''

# Create a new string with no whitespace 
day = '  TUESDAY   ' 
new_day = day.strip()# test to see if it took out the spaces
# print(len(day))#printed length to compare changes
# print(len(new_day))



'''Indexing, with square brackets'''

word = 'Jasmine'
first_letter_of_word = word[0]
# print(first_letter_of_word)
# print(word[1])
# print(word[2])
# print(word[3])
# print(word[4])
# print(word[5])
# print(word[6])
# print(word[8])#creates an error because there is no 8th letter
#IndexError: string index out of range (what it says in terminal)


'''****************************************'''

# Create a variable to capture the first letter of this string
greeting = 'whatssup!'
first_position_letter = greeting[0]
#print(first_position_letter)
#print(first_position_letter.upper())#just testing upper()

# Grab the last letter in a variable
last_letter_of_greeting = greeting[-1]# -1 will print the last character
'''last_letter_of_greeting = greeting[len(greeting)-1] that will give you the last position of a STRING'''
#print(last_letter_of_greeting)


# Using the length and bracket notation, access the last letter in the variable below
month = 'February'
last_position = month[-1]
#print(last_position)



# Using bracket notation access the letter x, the letter e, and the letter d 
first_name = 'Alexandra'
find_x_position = first_name.find('x')# use find to find the position of a character if unknown
# print(find_x_position)
# find_x = first_name[3]
# print(find_x)

find_e_position = first_name.find('e')
# print(find_e_position)
# find_e = first_name[2]
# print(find_e)

find_d_position = first_name.find('d')
# print(find_d_position)
# find_d = first_name[6]
# print(find_d)





'''Reverse indexing'''
fav_animal = 'Ostrich'
# print(fav_animal[-1])
# print(fav_animal[-2])
# print(fav_animal[-3])
# print(fav_animal[-4])
# print(fav_animal[-5])
# print(fav_animal[-6])
# print(fav_animal[-7])
# print(fav_animal[-8])# IndexError: string index out of range (line 120)



# Using bracket notation and reverse indexing, access the letter g, the letter i, the letter p
fav_season = 'spring'

find_g= fav_season[-1]
find_i= fav_season[-3]
find_p = fav_season[-4]

print(find_g)
print(find_i)
print(find_p)



''' Slicing '''
# There are 3 parameters available with indexing with bracket notation [start:stop:step]
fav_food = 'spaghetti'



# Using slicing please create a string that accesses 'rica' in 'America'

country = 'America'



# Using slicing please create a string that accesses 'ora' in 'Dora the explorer'
cartoon = 'Dora the explorer'


# Using slicing please create a string that accesses 'explo' in 'Dora the explorer'


# Using slicing please create a string that accesses 'albo' in 'Rocky Balboa'
boxer = 'Rocky Balboa'



# Let's step through this string 2 characters at a time
superheroine = 'Wonder Woman'


# Lets step through this entire word and skip by 4
word = 'Supercalifragilisticexpialidocious'


'''Slicing in reverse 
Refer to slice image as a guide if needed

'''


'''

D A Y C A R E
0 1 2 3 4 5 6


D   A   Y   C   A   R   E
-7 -6  -5  -4  -3  -2  -1

'''
random_word = 'daycare' 

# Fun with reverse indexing
# print(random_word[1:0:-1]) # a
# print(random_word[2:0:-1]) # ya
# print(random_word[4:0:-1]) # acya
# print(random_word[5:0:-1]) # racya
# print(random_word[6:0:-1]) # eracya
# print(random_word[7:0:-1]) # eracya
# print(random_word[8:0:-1]) # eracya




'''
Write some code to print the second half of a string.
Example:
python
hon
'''



# End Parameter
# print('Hello', end=' ')
# print('World', end='')
# print('!', end='\n')


# Sep Parameter
# print("Today I woke up at ", 8, " am", sep='*')

'''
Get input from the user and store it in a variable called userin.
Then print the user input. The output should follow exactly this format, including the colon and period at the end:
You entered: userin.
Where userin is what you got from the user.
You must format the print statement like this:
print("You entered",userin)
How can you add sep and end keywords to get the exact formatting shown above?
'''


'''
You need to write a script that will generate an email to a customer who has just made a purchase. You have 3 variables:
name, which stores the customer's name as a string
product, which stores the product name as a string
price, which stores the price of the product as a float
Use an f-string to generate an email message with the following text, and print it. Make sure to round the price to 2 decimal places. The email should be one multi-line string.
Dear {name},
Thank you for your purchase of a {product}. Your credit card has been charged ${price}.
We appreciate your business and look forward to serving you again.
Sincerely,
The ABC Company
'''

name = 'Josiah Wilson'
product = 'ABC Sneakers'
price = 74.95343452342





'''
Write some code that takes a string and tells if it is a palindrome (same forwards and backwards).
Hint: Use indexing/slicing and boolean expressions

Examples:
racecar: True
cat: False
'''

