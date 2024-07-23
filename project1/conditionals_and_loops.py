''' Loops and Conditionals

What is the difference between a For and While Loop?

For Loops help us loop through interables (strings, lists, tuples). While loops allow us to effectively target conditions. break keyword gets you out of the loop immediately


    
    
How do I write a For Loop?


animal = 'dog'

for a in animal:
    print(a)

Result:
d
o
g

How do I write a While Loop?

start = 0
end = 10

while start <= end:
    print(start)
    start += 1

'''


''' Break Keyword

Break is a keyword that when placed in a loop will leave the loop without executing any more code when the keyword is reached.

In example 1, we have to re-enter the loop after the stop condition is entered by the user

In example 2, we are able to break out of the loop as soon as we fulfill our condition

'''
# Example 1
#Initializing the variable
userin = ''

# while userin != 'stop':
#     userin = input("Please enter your text or type \'stop\' to stop: ").casefold()
#     print('We are going back to try to re-enter the loop, and test your input')

# Example 2
# userin = ''

# while True:
#     userin = input("Please enter your text or type \'stop\' to stop: ").casefold()
#     if userin == 'stop':
#        print('Goodbye, I am stopping now')
#        break #once user has put in password, username use break



'''
Write some code that takes in numbers from a user one at a time. This should keep going until the user enters 0. Then print the sum of all the numbers. If the user inputs something that isn't a number, an error message should appear and the program should stop. (Hint: use break)

Example (no error):
5
12
0
Sum: 17

Example (error):
5
7
c
Error: Not a number
'''

#Initialize any needed variables
total = 0

#Start a loop
# while True: 
# #Get data from the user
#     userin = input('Please enter a number: ')
    # print(userin)
    

#Python isnumeric testing to check if valid
#     if not userin.isnumeric():
#         print("Error: Not a number")
#         break
# # if ewusl to zero, we print the sum and than we are done
#     if userin == '0':
#         print(f'Sum: {total}')

#     else:
#         total += int(userin)# add the total so user sees result   

#If its a number, add to a running sum
    

#if it is some other character, we stop, print error message



'''5 Letter Word Program
Create a program which accepts only words with 5 letters. If the user inputs any other word with more than or less than 5 letters, force them to start over again. If the word has 5 letters, congratulate the user on inputting a 5 letter word
'''
#program can only accept words with 5 letters
# while True:
# # Initialize variable

#     userword = input('Type a 5 letter word: ')

#     if len(userword) != 5:

# #congratulate the user on inputting a 5 letter word
#         print("Word is not 5 letters")
#         continue
#     else:
#         print("Awesome job!")
#         break
          
'''
Example

Use the continue keyword to loop through a string and only print the vowels.

'''
# my_string = 'Saturday'
# vowels = 'aeiou'

# for m in my_string:
#     if m in vowels:
#         print(m)
#         continue


'''

Exercise: Sum of even digits

Take a string as user input, and verify that it's a number.
Loop through each digit of the number, and only add it to the sum if it's even.
Print the sum of all the even digits at the end. 
Make sure to use the continue keyword.
'''
#initalize variable

sum = 0
#Loop through each digit of the number
# while True:
    
#     user_in = input("Please type in your passcode: ")
    
#     if user_in.isnumeric():
#         for u in user_in: # we are looping through the user input
#             u = int(u) # convert to int
#             if u % 2 == 0: # if our number is even
#                 sum += u # add all even numbers to sum
#                 continue #allow us to append even numbers to sum
#             print(sum)
#     else:
#         print("Please enter a valid number to continue")


#add digits to sum only if its even

#print sum of all even digits
#print('sum')



''' Break vs. Continue '''

word = 'hello'
vowels = ['a', 'e', 'i', 'o', 'u']

# for w in word:
#     if w in vowels:
#         print(w)
#         break


# for w in word:
#     if w in vowels:
#         print(w)
#         continue


''' Pass keyword - placeholder'''

season = 'summer'

# for s in season:
#     pass


'''

Write some code that takes in strings from a user one at a time.
After each string is taken in evaluate if the string is empty, a number, a set of letters, or contains symbols.
If the string is empty, stop the loop.
If the string is a number, convert it to a float and add it to a total.
If the string is a set of letters, concatenate to the other letter strings passed in.
If it contains a symbol, or is none of the above, do nothing and repeat the loop.
Make sure to use break and/or continue.
'''

''' Let's Make a Plan'''

''' Following the plan '''
# initialize variables to capture string and total
total = 0
output = ''
# start loop
while True:
    pass
# get string
    userin = input('Please enter letter: ')
# If the string is empty, stop the loop
    if userin == '':
        print('Empty String')
        break
# If the string is a number, convert it to a float and add it to a total
    if userin.isnumeric():
        userin = float(userin)
        total += userin
        print(f'your total is {total}')
        continue

# If the string is a set of letters, concatenate to the other letter strings passed in.
    if userin.isalpha():
        output += userin
        print(f'Your string is {output}')
        continue
        

# If it contains a symbol, or is none of the above, do nothing and repeat the loop
    if not userin.isalnum():
        

''' Following the plan '''



''' While Else and For Else

Discussion:
What is the output of this code?
What would the output be if i is initialized to 6?

'''

# i = 3
# while i > 0:
#     print(i)
#     i -= 1
#     if i == 4:
#         break
# else:
#     print('done')


''' More fun while true!

Write a while true loop that will keep asking the day of the week until you type in Monday

'''

