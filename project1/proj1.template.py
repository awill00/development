# import re NOT SURE IF I NEED IT
''' Print statement outlining rules for your application'''
print("\n \nPlease create password and username. \n Username must start with a lowercase letter, contain letters, numbers and underscores. \n Username can not be an existing username. \n \n Passwords must be 8  to 12 characters long.\n Passwords must contain uppercase and lower case letters, \n a number, and these characters: !,?, @, #, $, ^, &, *, _ \n")
 


''' Initialize your variables 


We will need 2 variables to capture the username and password. Another 2 variables to use as the system username and password to authenticate against when we register
'''
username_saved = ''
password_saved = ''

''' A List to handle error messages '''

error_code = ['Username must start with a lowercase letter, contain letters, numbers and underscores \n Username can not be an existing username.',

'Username already exists!',
 
'Passwords did not match, Please enter password',

'Passwords must be  8 or more',
'Password must be 12 characters or less.',

'Passwords must contain uppercase and lower case letters.'
'Passwords must contain these characters: !,?, @, #, $, ^, &, *, _'
]


admin_usernames = ['admin','admin123','user1', 'superuser']
special_characters = ['!','?', '@', '#', '$', '^', '&', '*', '_']

''' Start your while loop '''

while True:
  #Get your username and password
  username_input = input('Please enter user name: ' )
  
#Test your username and enforce logic
  for u in username_input:
    if username_input[0].lower():
       print('username starts with lower letter check!')
      
       if username_input not in admin_usernames:
        print('username not in admin list check!')
        
        if username_input.isalnum(): 
         print('username has alpha numeric characters check!') 
         username_saved = username_input
         print(f'The testing username  {username_saved} was saved check!')
         #break is the way to stop multiple output and was tested so check!
         password_input = input('Please create a password: ')

         for p in password_input:
            if len(password_input) < 8:
                 print(error_code[3])
                 
            # else:
            #   print('password checked for 8 character minumum!')     
            elif len(password_input) > 12:
                 print(error_code[4])
            # else:
            #    print('password checked for 12 character maximum')     
         for p in special_characters:
                if p in password_input:
                 print('password special characters where checked!')
                # else: 
                #  print('no special characters in password')     
    #             #this is going to lead to next step which is the user signing in with password and username   
                 
                 for n in password_input:
                      if password_input.isupper():
                       print('password contains at least one upper character')
                      else:
                         print('no uppercase') 
                      
                #   break
    #               if password_input.islower():
    #             #  print('password contains at least one lower letter') 
    #                password_saved = password_input
    #                print(f'The username {username_saved} and password successfully saved!')
    #                break
    #               else:
    #                  print(error_code[5])
             
    #    #convert the password_saved and username_saved into dictionary and have the user register
        
    # elif username_input != '_': 
    #   print(error_code[0])
    #   continue
    
  
# Test your password and enforce logic
  
  
  

# If we pass, congratulate the user and immediately ask them to register

  # print(f'Thank you {username}! Please register')


#If they input the correct matching info, program complete. If incorrect, send the user all the way back to the beginning of the loop to start from scratch. 


#result = dict(zip(username_saved, password_saved)) this is for combining password and username
