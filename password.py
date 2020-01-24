class Users:
    """
    Class that generates new instances of users
    """
    user_list = [] #Empty user list

    def __init__(self,user_name,password):
    
        '''
        __init__ method that helps us define properties for our users.
        '''
        self.user_name = user_name
        self.password = password
    
    def save_user(self):
            
        '''
        save_user method saves user objects into user_list
        '''
            
        Users.user_list.append(self)
        
    def delete_user(self):
        
        '''
        delete_user method deletes a saved user from the user_list
        '''
    
        

class Credentials:
    """
    Class that generates new instances of user credentials
    """
    credential_list = [] #Empty credential list
    
    def __init__(self, user_name, account, account_username, account_password):
    
        '''
        __init__ method that helps us define properties from our user credentials.
        '''
        self.user_name = user_name
        self.account = account
        self.account_username = account_username
        self.account_password = account_password
        
    def save_credential(self):
         
        '''
        saves the inputed credentials
        '''
        
        Credentials.credential_list.append(self)
    
    @classmethod
    def display_credential(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list
         
        
    @classmethod
    def find_by_username(cls,name):
        '''
        method that takes in a username and returns the user credentials that matches the username.
        
        Args:
            name: user name to search for credential
        Return :
            Credential of person that matches the username.    
        '''
        for credential in cls.credential_list:
            if credential.user_name == name:
                return credential
            
    def delete_credential(self):
        
        '''
        delete-credential method deletes a saved credential from the credential_list
        '''
        
        Credentials.credential_list.remove(self)
    
    @classmethod
    
    