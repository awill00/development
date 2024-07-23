
''' Print statement outlining rules for your application'''
print("\n \nPlease create password and username. \n Username must start with a lowercase letter, contain letters, numbers and underscores. \n Username can not be an existing username. \n \n Passwords must be 8  to 12 characters long.\n Passwords must contain uppercase and lower case letters, \n a number, and these characters: !,?, @, #, $, ^, &, *, _ \n")
 


''' Initialize your variables 


We will need 2 variables to capture the username and password. Another 2 variables to use as the system username and password to authenticate against when we register
'''
username_saved = ''
password_saved = ''

''' A List to handle error messages '''

error_code = ['Username must start with a lowercase letter, contain letters, numbers and underscores \n Username can not be an existing username.',

'Username or Password is not correct, Please enter username and password',
 
'Passwords must be  8 or more',
'Password must be 12 characters or less.',

'Passwords must contain uppercase', 
'Passwords must contain lower case letters.',
'Passwords must contain these characters: !,?, @, #, $, ^, &, *, _',
'Password must contain numbers'
]


admin_usernames = ['admin','admin123','user1', 'superuser']
special_characters = ['!','?', '@', '#', '$', '^', '&', '*', '_']

''' Start your while loop '''

while True:
  #Get your username and password
  username_input = input('Please enter user name: ' )
  
#Test your username and enforce logic
  
  if not username_input[0].islower():
      print(error_code[0])
      
  if username_input not in admin_usernames:
      print('username not in admin list check!')
        
  if username_input.isalnum() or (special_characters[8] in username_input): 
      print('username has alpha numeric characters check!') 
        
  username_saved = username_input
  print(f'The testing username  {username_saved} was saved check!')
    
   # Test your password and enforce logic
   
  password_input = input('Please create a password: ')

  
  if len(password_input) < 8:
      print(error_code[3])
                     
  elif len(password_input) > 12:
      print(error_code[4])
           
  for p in special_characters:
    if p in password_input:
      print('password special characters where checked!')

    if p.isalnum(): 
      print('There are letters and numbers')  
    elif p.isupper():
      print('there is an uppercase letter checked!')
    elif p.islower():
      print('there is a lowercase letter checked')
    password_saved = password_input
    print(f'The username {username_saved} and password successfully saved!')
    break
                       
    # If we pass, congratulate the user and immediately ask them to register 
  user_signin = input('Thank you!\n\nPlease sign in with username: ')
  if user_signin == username_saved:
      print('username correct!')
  password_signin = input('Please enter password: ')
    
  if user_signin != username_saved and password_signin != password_saved:
    print(error_code[1])

  if user_signin == username_saved and password_signin == password_saved:
    print(f'Welcome back {username_saved}!')
    break
    
    #If they input the correct matching info, program complete. If incorrect, send the user all the way back to the beginning of the loop to start from scratch. 
#    else:
    #   print(error_code[0])      
    #   continue
