from typing import ContextManager
from user import  User, Validator

# welcome and create account user, pin and password for manager.
# Save account details in dictionary.
maccounts = {'uid': }
user_ok = False
while not user_ok:
    
    # Welcome manager and take user input.

    
    muser = input('Enter desired username: ')
    user_check = User(user_name=muser)
    validate_user = Validator(user_name=user_check.user_name)

    if validate_user.Name_Checker() == None:
        print('Username is not a valid name, please try again')
        user_ok = False
        
    else:
        print(f'Hi {validate_user.Name_Checker()}.\nPlease enter pin and password.')
        user_ok = True

pin_ok = False
while not pin_ok:

    upin = input('Desired pin: ')

    pin = User(user_pin=upin)
    validate_pin = Validator(user_pin=pin.user_pin)

    if validate_pin.ID_check(4) == 'None':
        print('Pin is not a valid pin, please try again')
        pin_ok = False
    else:
        print(f'Hi {validate_user.Name_Checker()}.\nPlease enter password.')
        pin_ok = True



            


            

    
        
        

    




