class Person():
    ''' A Class representation of a person
 
        Takes 3 argument.
 
        Methods:
            Constructor:
            < __init__() >
 
 
        Parameters:
            user_id, user_email, user_name
         '''
 
    def __init__(self, user_id, user_name, user_email):
        '''Initialising  the Person class attributes.'''
 
        self.user_id = user_id
        self.user_email = user_email
        self.user_name = user_name
 
class Instructor(Person):
    """ A class representation of Instructor.
 
        Inherits attributes of the Person class.

        Methods:

            Constructor:
            < __init__() >
            
            displayInformation:
                ID with a default value of 'Unknown'
                Name with a default value of Unknown'
                Email with a default value of 'Unknown'
                Institution with a default value of 'Unknown'
                Degree with a default value of 'Unknown'
        """

 
    def __init__(self, user_id = 'Unknown', user_name = 'Unknown', user_email = 'Unknown', study = 'Unknown', 
    institute='Unknown', degree='Unknown'):
        '''
        Initialising attributes of the parent class.
        Then initialize attrs specific to Instructor class
        
        '''
 
        super().__init__(user_id, user_name, user_email)
        self.institute = institute
        self.degree = degree
    
    # Display instructos information.
    def displayInformation(self):
        ''' A method to display instructor information. '''
 
        print('ID is:', self.user_id)
        print('Name: ', self.user_name)
        print('Email: ', self.user_email)
        print('Institution: ' + self.institute)
        print('Degree: ' + self.degree)

class Student(Person):
    """ A class representation of student.
 
        Inherits attributes of the Person class.

        Methods:

            Constructor:
            < __init__() >
            
            displayInformation:
                ID with a default value of 'Unknown'
                Name with a default value of Unknown'
                Email with a default value of 'Unknown'
                study with a default value of 'Unknown'
                
        """
 
    def __init__(self, user_id = 'Unknown', user_name = 'Unknown', user_email = 'Unknown', study = 'Unknown'):
        '''
        Initializing attributes of the parent class.
        Then initialize attrs specific to Student class
        
        '''
        super().__init__(user_id, user_name, user_email)
        self.study = study
 
    # Displaying student information.
 
    def displaystudentInfo(self):
        ''' A method to display student information. '''
        print('ID is:', self.user_id)
        print('Name: ', self.user_name)
        print('Email: ', self.user_email)
        print('Course: ', self.study)
 
 
class Validator():
    """ A class representation of user input validation.
 
        Inherits attributes of the Person class.

        Methods:

            Constructor:
            < __init__() >
            < Email_Checker >
            < ID_check >
            < Name_Checker >
            < institution_Checker >
            < Degree_Check >
            < Study_Checker >
            
        All attributes of the class has default value of empty string.
        """

    def __init__(self, user_id='', user_name='', user_email='', study ='', institute='', degree=''):
        '''Initialising attributes for Validator class'''
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email
        self.institute = institute
        self.degree = degree
        self.study = study
        self.bad_chars = '!"@#$%^&*()_=+,<>/?;:[]{}\)'
        self.bad_characters = '!"\'#$%^&*()=+,<>/?;:[]{}\)'

    
    def Email_Checker(self):
        """
        Description:
            Method checks user email and returns <Email address> .
            
            Method returns  in event of bad character in email address.
        """
            
        if self.user_email:
            
            
            self.user_email = self.user_email.strip()
            
            # Using for loop 
            for char in self.user_email:
                
                # if character in email not in bad characters, continue the checks on the remaining characters in email.
                
                if char not in self.bad_characters:
                    
                    continue
                    
                # If character in email is found in bad characters
                    
                else:
                    
                    # Exit the function.
                    
                    return
                
        # Else email address field cannot be left blank.
        
        else:
            
            
            return
            
        # Return email address.
        
        return self.user_email
 
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
 
    def institution_Checker(self):
        """
        Description:
            Method checks Institution  and returns <valid Institution> .
            
            Method returns if blank value is supplied.
        """
 
        if self.institute:

            return self.institute
        else:
            return
    
    def Degree_Check(self):

        """
        Description:
            Method checks degree  and returns <valid degree> .
            
            Method returns if blank value is supplied.
        """

        

        if self.degree:

            return self.degree

        else:

            return

    def Study_Checker(self):
        """
        Description:
            Method checks study  and returns <valid study> .
            
            Method returns if blank value is supplied.
        """
        if self.study:

            return self.study

        else:

            return

