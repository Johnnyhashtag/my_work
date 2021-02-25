
from user import  User, Validator

# welcome and create account user, pin and password for manager.
# Save account details in dictionary.
maccounts = {}
user_ok = False

# Ask user for input and check that requirement for each input are met.
while not user_ok:
    
    # Welcome manager and take user input.
    print('Welcome!')    
    muser = input('Enter desired username: ')
    user_check = User(user_name=muser)
    validate_user = Validator(user_name=user_check.user_name)

    if validate_user.Name_Checker() == None:
        print('Username is not a valid name, please try again')
        user_ok = False
        
    else:
        print(f'Hi {validate_user.Name_Checker()}.\nPlease enter pin and password.')
        user_ok = True

# Ask user for desired pin and do a pin validation check.

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

# Ask user for desired password and do a password validation.
pwd_ok = False
while not pwd_ok:

    pwd = input('Desired pass: ')

    password = User(pass_wd=pwd)
    validate_pwd = Validator(user_pwd=password.pass_wd)

    if validate_pwd.Pass_Checker() == None:
        print('Password is not acceptable pass, please try again')
        pwd_ok = False
    else:
        print(f'Hi {validate_user.Name_Checker()}.\nYour username, password and pin is now been saved.')
        pwd_ok = True
    
maccounts[validate_user.Name_Checker()] = [validate_pin.ID_check(4), validate_pwd.Pass_Checker()]

# Managers login, create and management area
prompt = f'Welcome {validate_user.Name_Checker()} to account management services.\n'
prompt += 'please choose a service.\nC to create - M to manage - L to login'

print(prompt)

service_ok = False
while not service_ok:

    service = input('Please choose a service: ')

    if service.lower() == 'l':

        user_login = input('User login: ')

        




            


            

    
        
        

    




