from name_function import full_formatted_name
while True:
    
    f_name = input('Enter first name: ')
    if f_name.lower() == 'q':
        break

    l_name = input('Enter last name: ')
    if l_name.lower == 'q':
        break
    
    middle_name = input('Enter middle name: ')
    if middle_name.lower() == 'q':
        break
    formatted_name = full_formatted_name(f_name, l_name, m_name=middle_name)
    print(f'\t Neatly formatted name: {formatted_name}')
