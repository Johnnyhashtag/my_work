class User():

    """Initialise User class"""

    def __init__(self, user_name='unknown', pass_wd='unknown', user_pin='unknown'):
        self.user_name = user_name
        self.pass_wd = pass_wd
        self.user_pin = user_pin

    def user_Name(self):
        return self.user_name
    
    def user_Pass(self):
        return self.pass_wd
    
    def user_Pin(self):
        return self.user_pin

class Validator():
    """ A class representation of user input validation.
 
        Inherits attributes of the Person class.

        Methods:

            Constructor:
            < __init__() >
            < ID_check >
            < Name_Checker >
            
        All attributes of the class has default value of empty string.
        """

    def __init__(self, user_id='', user_name=''):
        '''Initialising attributes for Validator class'''
        self.user_id = user_id
        self.user_name = user_name
        self.bad_chars = '0123456789!"@#$%^&*()_=+,<>/?;:[]{}\)'
 
    def ID_check(self, max_length):
        """
        Description:
            Method checks user ID for maximum length and returns <user ID> .
            
            Method returns in event of bad character in userID.
        """
        
        if self.user_id:
            
            
            
            # if all characters in str(id) is an integer.
            if self.user_id.isnumeric():
                
                # Check if length of id supplied is less than or equal to maximum length.
                # Return ID
                if len(self.user_id) <= max_length:

                    return self.user_id
                    
                
                # exit 
                else:
                    
                    return 'None'
            
            # exit
            else:
                
                return 'None'
                
        # exit
        else:
            
            return 'None'
 
    def Name_Checker(self):
        """
        Description:
            Method checks user name for validity and returns <valid name> .
            
            Method returns nothing in event of bad character in name.
        """
	
        # Strip of whitespaces from name.
        self.user_name = self.user_name.strip()
        
        # Making sure name argument supplied at call to function is not an empty string.
        
        if self.user_name:
            
            # using for loop to iterate over the characters in name
            for chars in self.user_name:
                
                # Make sure no bad characters in name using 'not in' to check.
                if chars not in self.bad_chars:
                    
                    
                    continue
                
                # else exit.
                else:
                    
                    return
            
        # else exit.
        else:
            
            return
        
        # return name in title case.
        return self.user_name.title()
 
