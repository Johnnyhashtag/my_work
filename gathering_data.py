# Import modules

from person import Person, Instructor, Student, Validator

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
                print('UserID is not valid, please try again')
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
            
 
            if validate_student.Email_Checker() == 'None':
                print('Email address is not a valid email, please try again')
 
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
 
            if validate_student.Name_Checker() == 'None':
                print('Name is not a valid name, please try again')
 
                name_ok = False
 
            else:
 
                college_records.append(validate_student.Name_Checker())
 
                name_ok = True
        
        # Get students study and check for validity.
        # Append valid study to college records.
        study_ok = False
        while not study_ok:
 
            study_program = input('Enter Student Study:')
 
            student = Student(study= study_program)
            validate_student = Validator(study= student.study)
 
            if validate_student.Study_Checker() == 'None':
                print('Study can not be blank, please try again.')
 
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
            
            
            if validate_instructor.ID_check(5) == 'None':
                print('UserID is invalid, please try again.')
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
            
 
            if validate_instructor.Email_Checker() == 'None':
                print('Email address is not a valid email, please try again')
 
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
 
            if validate_instructor.Name_Checker() == 'None':
                print('You have entered an invalid name, please try again')
 
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
 
            if validate_instructor.institution_Checker() == 'None':
                print('Institution can not be blank, please try again')
 
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
 
            if validate_instructor.Degree_Check() == 'None':
                print('Highest degree is required, please try again')
 
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