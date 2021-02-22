from user_acct import  User, Validator

# welcome and create account user, pin and password for manager.
# Save account details in dictionary.
maccounts = {}
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

    
        
        

    




