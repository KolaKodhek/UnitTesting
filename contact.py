class Contact:
    '''
    A class that generates new intances of contacts 
    '''
    
    contact_list=[]
    
    def __init__(self, first_name,last_name, email) -> None:
        '''
            first_name: New contact's first name
            last_name: New contact's last name
            email: New contact's email
        '''
        self.first_name= first_name
        self.last_name= last_name
        self.email= email
    
    def save_contact(self):
        '''
            This method saves new contacts into the contact list
        '''
        Contact.contact_list.append(self)