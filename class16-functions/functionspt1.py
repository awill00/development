''' Focus on the structure of your functions, let's have fun and learn how they work! :) '''


'''
1. Write as function that converts celsius to fahrenheit
''' 
#fahrenheit = (celsius * 9/5) + 32
#snake case for function names
# def find_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     print(fahrenheit)

# celsius = 20  # declaring variable  
# find_fahrenheit(celsius)


######## with input from user #########
# def convert_c():
#     celsius = float(input("Enter the temperature in celsius: "))
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"The temperature in fahrenheit is: {fahrenheit}" )
 
# convert_c()





''' 2. write a function that generates a filename of lastname, firstname, and todays date'''
from datetime import date


firstname = 'bill'
lastname = 'smith'

def filename_gen(fname, lname):
   return f'{lname}_{fname}_{date.today()}.txt' 
   

result = filename_gen(firstname, lastname)
# print(result)


'''  3. Function to add two different numbers '''

# num1 = 5
# num2 = 8

# def number_adder(val1, val2):
#    return val1, val2

# print(num1, num2 )



'''   4. Function to reverse a word for example 'team' becomes 'maet' '''

# word = 'team'

# def rev_word (word):
#    return word[::-1]



'''  5. Function that will deliver the average of 2 values '''





''' 
 6. Write a function that will loop through a string and print whether a character is or is not a vowel.
'''
# word = 'hooray'

# def vowel_check(word):
   
#     vowels = 'aeiou'
    
#     for w in word:
#        if w in vowels:
#           print(f'{w} is a vowel')
#        else:
#           print('is not a vowel')   
       
# vowel_check(word)


'''  7. Write a function that takes a list of these dictionary items. Return the first names from the list of dictionaries in a single list

students = [{'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 22}, {'name': 'Charlie', 'age': 21}]'''

students = [{'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 22},
            {'name': 'Charlie', 'age': 21}]


# def first_name(students): # this function accepts a list of dictionaries
#    output = [] # this will hold first names
#    for s in students:
#       name = s['name']
#      #  age = s['age']
#       output.append(name)
#    return output

# students_first_names =  first_name(students)

# print(students_first_names)
# print(type(students_first_names))
      


''' Let's print from our functions'''

''' 8.  Create a function that asks the user for their name and greets them back with a hello'''

def say_hello(fname, lname):
   print(f'Hello {fname} {lname}')

# say_hello(input('Type in your name'), input('Type in your last name'))   



''' If we print we return none'''
def show_none(word):
   print(word)
print(show_none('hello'))#print statement will show the return value   


''' 9.  Write a function that takes a list of students grades, return a dictionary with the students names and grade averages

students = [{'name': 'Alice', 'science':75, 'math':80, 'world history': 90},\
            {'name': 'Bob', 'science':50, 'math':65, 'world history': 88},\
            {'name': 'Charlie', 'science':100, 'math':75, 'world history': 70}]

'''

students = [{'name': 'Alice', 'science': 75, 'math': 80, 'world history': 90},
            {'name': 'Bob', 'science': 50, 'math': 65, 'world history': 88},
            {'name': 'Charlie', 'science': 100, 'math': 75, 'world history': 70}]

# def gpa(students):
#    grade_averages = {}
   
#    for s in students:
#       name = s['name']
#       science = s['science']
#       math = s['math']
#       world_history = s['world history']
#       gpa = (science + math + world_history) / 3
#       grade_averages.update({name:gpa})
#    return grade_averages
# report_card = gpa(students)   

#################### Cain's Code ##################

# from statistics import mean
# def gpa(student):
#     output = {}
#     for s in student:
#         name = s["name"]
#         grades = [s["science"], s["math"], s["world history"]]
#         gpa = mean(grades)
#         output[name] = gpa
#     return output
# print(gpa(students))

'''

10.
Suppose you work for a bank, and you have a list of transactions with the following information for each one: customer ID, transaction amount, and transaction type (deposit or withdrawal).
Write a function that takes in the list of customer transactions and returns a dictionary where the keys are the customer IDs and the values are the total transaction amounts for each customer.
Example:

transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'}]
     Output: {'a': 50, 'b': 350}
'''

transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},
                {'id': 'b', 'amount': 1350, 'type': 'deposit'},
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'},
                {'id': 'a', 'amount': 1000, 'type': 'deposit'},
                {'id': 'a', 'amount': 75, 'type': 'deposit'},
                {'id': 'a', 'amount': 60, 'type': 'deposit'},
                {'id': 'b', 'amount': 13, 'type': 'withdrawal'}]

#customer ID, transaction amount, and transaction type (deposit or withdrawal)

# Write a function that takes in the list of customer transactions  

def customer_actions(transactions):
   pass

# returns a dictionary where the keys are the customer IDs 

# (customer_id: total_transaction_amounts)

# values are the total transaction amounts for each customer.