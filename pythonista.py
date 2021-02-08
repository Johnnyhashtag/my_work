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
        self.bad_chars = ('!"@#$%^&*()_=+,<>/?;:[]{}\)')
        self.bad_characters = ('!"\'#$%^&*()=+,<>/?;:[]{}\)')

    
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

college_records = []
# Start of while loop
while True:
 
    # Offer user an option.
 
    print('Please type (1) for Student\nPlease type (2) for Instructor.')
    user_input = input('Please enter a number: ')
    
    # Perform error check on user input
    try:
        # Changing string input into integer
        user_input = int(user_input)

    except:
        continue
    
    # if user input equal to 1 gather student data.
    # check for validity and append it to list before asking for the next information.
    if user_input == 1:

        # Get student id and check for validity.
        # Append valid ID to college records.
        uid_ok = False
        while not uid_ok:

            sid = input('Enter Student ID: ')
            student = Student(user_id = sid)
            validate_student = Validator(user_id = student.user_id)
            
            if validate_student.ID_check(7) == 'None':
                print('UserID is not valid, try again')
                uid_ok = False
            
            else:
                college_records.append(validate_student.ID_check(7))
                uid_ok = True
        
        # Get students email and check for validity.
        # Append valid email to college records.
        email_ok = False
        while not email_ok:
            email = input('Enter Student Email:')

            student = Student(user_email= email)
            validate_student = Validator(user_email = student.user_email)
            

            if validate_student.Email_Checker() is None:

                email_ok = False

            else:

                college_records.append(validate_student.Email_Checker())

                email_ok = True
        
        # Get students name and check for validity.
        # Append valid name to college records.
        name_ok = False
        while not name_ok:

            name = input('Enter Student Name:')
            student = Student(user_name= name)
            validate_student = Validator(user_name= student.user_name)

            if validate_student.Name_Checker() is None:

                name_ok = False

            else:

                college_records.append(name)

                name_ok = True
        
        # Get students study and check for validity.
        # Append valid study to college records.
        study_ok = False
        while not study_ok:

            study_program = input('Enter Student Study:')

            student = Student(study= study_program)
            validate_student = Validator(study= student.study)

            if validate_student.Study_Checker() is None:

                study_ok = False

            else:

                college_records.append(validate_student.Study_Checker())

                study_ok = True

        # Confirm data has been appended to college records.
        # Give user the option to continue saving or quit.
        print('Student data appended to college records.')
        save_more = input('Type (Y/N) to make another entry: ')
        if save_more.lower() == 'y':
            continue
        else:
            print(college_records)
            break

    # elif user input equal to 2 gather instructors data.
    # check for validity and append it to list before asking for the next information.
    elif user_input == 2:
        
        # Get instructors id and check for validity.
        # Append valid ID to college records.
        uid_ok = False
        while not uid_ok:

            Iid = input('Enter Instructor ID: ')
            instructor = Instructor(user_id = Iid)
            validate_instructor = Validator(user_id = instructor.user_id)
            
            
            if validate_instructor.ID_check(5) is None:
                uid_ok = False

            else:
                college_records.append(validate_instructor.ID_check(5))
                uid_ok = True
        
        # Get instructors email and check for validity.
        # Append valid email to college records.
        email_ok = False
        while not email_ok:
            email = input('Enter Instructor Email:')

            instructor = Instructor(user_email= email)
            validate_instructor = Validator(user_email = instructor.user_email)
            

            if validate_instructor.Email_Checker() is None:

                email_ok = False

            else:

                college_records.append(validate_instructor.Email_Checker())

                email_ok = True
        
        # Get instructors name and check for validity.
        # Append valid name to college records.

        name_ok = False
        while not name_ok:

            name = input('Enter Instructor Name:')
            instructor = Instructor(user_name= name)
            validate_instructor = Validator(user_name = instructor.user_name)

            if validate_instructor.Name_Checker() is None:

                name_ok = False

            else:

                college_records.append(validate_instructor.Name_Checker())

                name_ok = True

        # Get instructors institute and check for validity.
        # Append valid institute to college records.
        institute_ok = False
        while not institute_ok:

            institution = input('Enter Instructor Institute:')

            instructor = Instructor(institute=  institution)
            validate_instructor = Validator(institute=instructor.institute)

            if validate_instructor.institution_Checker() is None:

                institute_ok = False

            else:

                college_records.append(validate_instructor.institution_Checker())

                institute_ok = True
        
        # Get instructors degree and check for validity.
        # Append valid degree to college records.
        degree_ok = False
        while not degree_ok:

            highest_degree = input('Enter Instructor Degree:')

            instructor = Instructor(degree= highest_degree)
            validate_instructor = Validator(degree= instructor.degree)

            if validate_instructor.Degree_Check() is None:

                degree_ok = False

            else:

                college_records.append(validate_instructor.Degree_Check())

                degree_ok = True
        
        # Confirm data has been appended to college records.
        # Give user the option to continue saving or quit.
        print('Instructor data appened to college records.')
        save_more = input('Type (Y/N) to make another entry: ')
        if save_more.lower() == 'y':
            continue
        else:
            print(college_records)
            break
    
    # else if user input is not 1 or 2.
    # break.
    else:
        
        break
