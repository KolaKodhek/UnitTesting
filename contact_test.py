import unittest #This is to import the unittesting module
from contact import Contact
'''
We are testing for the following behaviours:
1. Allow us to Create new contacts with properties.

2. Save contacts.

3. Display contacts.

4. Delete contacts.

5. Display contact information.

'''
class TestContact(unittest.TestCase):
    '''
        This is the test class that defines the test case for contact class behaviour.
        args:
        unittest.TestCase:TestCase class that help in creating test cases.
    '''
    
    def setUp(self):
        '''
            Set up to run before each  test case.
        '''
        self.new_contact = Contact("Felix","George","Mailme@gmail.com")
        
    def test_init(self):
        '''
            test_unit test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_contact.first_name,"Felix")
        self.assertEqual(self.new_contact.last_name,"George")
        self.assertEqual(self.new_contact.email,"Mailme@gmail.com")
        
if __name__=='__main__':
    unittest.main()