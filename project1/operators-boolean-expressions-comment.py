# Operators, boolean Epressions and Comments

# I am a comment
temperatrue = 95 # I am an inline comment

# I am a standard single line comment
first_name = 'Thomas' ''' Multi line comment - inline'''
last_name = 'the Train' """ Inline comment with double quotes"""

'''
Everything between these quotes will be commente out
'''

# comment me

#length = 5
#width = 7

#perimeter = 2 * (length + width) #This is a perimeter of a rectangle

#print(perimeter) 


#converting fahrenheit to celsius

#fahrenheit = 89 

#celsius = (fahrenheit - 32) * 5/9 


#print(celsius)

# Add 5 to me

age = 25
age += 5 # adding 5 via shortcut operators
#print(age)

# Adding 10 years

year = 2024
year += 10
#print(year)


#Subtract 20
num_one = 55
num_one -= 20
#print(num_one)

#Subtract 15
num_two = 11
num_two -= 15
#print(num_two)

# Multiply by 3
my_value = 9
my_value *= 3
print(my_value)
# Multiply by 10
mileage = 15
mileage *= 10
print(mileage)

#Divide by 2
pizza_slices = 8
pizza_slices /= 2
print(pizza_slices)

# Raise to the 3rd power **
num_three = 6
num_three **=3
#print(num_three)

# Raise to the 2nd power **
data = 16
data **=2 
#print(data)

# Integer division, how many times does 3 go into 16? //
val_one = 16
val_one //= 3
#print(val_one)

# Integer divide by 4 //
val_two = 9
val_two //= 4
#print(val_two)


#Modulus we use often to find if a value is odd or even 
# Find the remainder if divided by 3 %
val_three = 10
val_three %= 3
#print(val_three)

# Find the remainder if divided by 5 %
val_four = 14
val_four %= 5
#print(val_four)

# Is 6 greater than 2? >
print(6 > 2)
result =(6 > 2)
print('Is 6 greater than 2?')

# Is 5 greater than or equal to 6? >=
print(5 >= 6)
result = (5 >= 6)
print('Is 5 greater than or equal to 6?')

# Is 5 equal to 5? ==
print(5 == 5)
result = (5 == 5)
print('Is 5 equal to 5?')

# Is 100 not equal to 75? !=
print(100 != 75)
result =(100 != 75)
print('Is 100 not equal to 75?')

#and
# print(5 == 5 and 4 == 4) # True
# print(2 == 2 and 3 == 1) # False
# print(1 == 2 and 2 == 10) # False

''''''
log_1 = (5 == 3)
log_2 = (4 == 7)
print('Log 1', log_1) #True
print('Log2', log_2)  #False
print('log 1 and Log 2',log_1 and log_2)

# or
print(5 == 5 or 5==3)# True if at least 1 is true

#not 
is_it_autumn = True 
print(not is_it_autumn)# inverts the answer

x= 5
y = 10

# is x less than y?
#print(x<y)

# Are we the same object. 'is' keyword

fname = 'Taylor'
first_name = 'Taylor'
print(fname is first_name)
print(fname == first_name)

# in
print('J' in 'January')
print('F' in March)


