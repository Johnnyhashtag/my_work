
from user import  User, Validator

# welcome and create account user, pin and password for manager.
# Save account details in dictionary.
#TODO: save user input into  database retrieve user data from database,more account management services.
maccounts = {'trey': ['1234', 'pass']}


# Managers login, create and management area
prompt = f'Welcome to account management services.\n'
prompt += 'please choose a service.\nC to create - M to manage - L to login'

print(prompt)

service_ok = False
while not service_ok:

    service = input('Please choose a service: ')

    if service.lower() == 'l':
        
        user_login_ok = False
        while not user_login_ok:

            user_login = input('User login: ')

            user_login_ojbect = User(user_name=user_login)
            validate_user_login = Validator(user_name=user_login_ojbect.user_name)

            if validate_user_login.Name_Checker() in maccounts.keys():
                print(f'Hi {validate_user_login.User_Name_Checker()}, Please enter your password:')
                user_login_ok=True

            else:
                user_login_ok = False


            user_password_ok=False
            while not user_password_ok:
                user_password = input('User password: ')

                user_password_ojbect = User(pass_wd=user_password)
                validate_pwd_object = Validator(user_pwd=user_password_ojbect.pass_wd)

                for key, value in maccounts.items():

                    if validate_pwd_object.Pass_Checker() in value:
                        print('Please enter your pin:')
                        user_password_ok=True


                        user_pin_ok=False
                        while not user_pin_ok:

                            user_pin_input = input('User pin: ')
                            user_pin_ojbect = User(user_pin=user_pin_input)
                            validate_pin_object = Validator(user_pin=user_pin_ojbect.user_pin)#
                                
                            for key, value in maccounts.items():
                                
                                if validate_pin_object.Pin_Checker(4) in value:
                                    print('Welcome to account home!')
                                    user_pin_ok = True

                                    another_service = input('Please choose (Y/N) for another service: ')
                                    if another_service.lower() == 'y':
                                        service_ok = False
                                    else:
                                        service_ok = True

                                else:
                                    print('Please check user pin.')
                                    user_pin_ok = False

                    else:
                        user_password_ok=False
    
    elif service.lower() == 'c':

        user_ok = False
        
        # Ask user for input and check that requirement for each input are met.
        
        while not user_ok:
            
            # Welcome manager and take user input.
            print('Welcome to account creation!')    
            muser = input('Enter desired username: ')
            user_check = User(user_name=muser)
            validate_user = Validator(user_name=user_check.user_name)

            if validate_user.User_Name_Checker() == None:
                print('Username is not a valid name, please try again')
                user_ok = False
        
            else:
                print(f'Hi {validate_user.User_Name_Checker()}.\nPlease enter pin and password.')
                user_ok = True

        # Ask user for desired pin and do a pin validation check.

        pin_ok = False
        while not pin_ok:

            upin = input('Desired pin: ')

            pin = User(user_pin=upin)
            validate_pin = Validator(user_pin=pin.user_pin)

            if validate_pin.Pin_Checker(4) == 'None':
                print('Pin is not a valid pin, please try again')
                pin_ok = False
            else:
                print(f'Hi {validate_user.User_Name_Checker()}.\nPlease enter password.')
                pin_ok = True

        # Ask user for desired password and do a password validation .
        pwd_ok = False
        while not pwd_ok:

            pwd = input('Desired pass: ')

            password = User(pass_wd=pwd)
            validate_pwd = Validator(user_pwd=password.pass_wd)

            if validate_pwd.Pass_Checker() == None:
                print('Password is not acceptable pass, please try again')
                pwd_ok = False
            else:
                print(f'Hi {validate_user.User_Name_Checker()}.\nYour username, password and pin is now been saved.')
                pwd_ok = True
                
                another_service = input('Please choose (Y/N) for another service: ')
                if another_service.lower() == 'y':
                    service_ok = False
                else:
                    service_ok = True
    
                maccounts[validate_user.User_Name_Checker()] = [validate_pin.Pin_Checker(4), validate_pwd.Pass_Checker()]



                    
















                    

    









            


            

    
        
        

    




