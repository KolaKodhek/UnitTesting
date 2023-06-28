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
    
    
    def tearDown(self) -> None:
        '''
            This method cleans the list after eery test is run.
            We added this method after our third test faild 
            since we already had 3 items in the list instead of 2.
            So to pass we had to clear the list after evey test.
        '''
        Contact.contact_list = [] 
        
           
    def test_init(self):
        '''
            test_unit test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_contact.first_name,"Felix")
        self.assertEqual(self.new_contact.last_name,"George")
        self.assertEqual(self.new_contact.email,"Mailme@gmail.com")
    
    def test_sava_contact(self):
        '''
            Since our first test to create a new 
            contact passed, we proceed to test if we can save the contact
        '''
        
        self.new_contact.save_contact()#Save's the contact
        self.assertEqual(len(Contact.contact_list),1)
        
    def test_save_multiple_contacts(self):
        '''
            We test if we can save multiple contacts in our contact list
        '''
        self.new_contact.save_contact()
        test_contact= Contact("Test", "User", "testuser@gmail.com")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)
        
    def test_delete_contact(self):
        '''
            Test to see if we can remove a contact from the list
        '''
        self.new_contact.save_contact()
        test_contact= Contact("Test", "User", "testuser@gmail.com")
        test_contact.save_contact()
        
        self.new_contact.delete_contact()#deletes the contact
        self.assertEqual(len(Contact.contact_list),1)
        
    def test_find_contact(self):
        '''
            Test to find if we can find a contact
        '''
        self.new_contact.save_contact()
        test_contact= Contact("Test", "User", "testuser@gmail.com")
        test_contact.save_contact()
        
        found_contact = Contact.find_by_first_name("Test")
        
        self.assertEqual(found_contact.email,test_contact.email)
        
if __name__=='__main__':
    unittest.main()