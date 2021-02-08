import unittest

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

    class TestNameCases(unittest.TestCase):

        def test_first_last_name(self):
            """Do names like l'bron  james work?"""
            working = full_formatted_name(f_name, l_name, m_name=middle_name)
            self.assertEqual(working, 'Ayobami John Haastrup')

    if __name__ == '__main__':
        unittest.main()



