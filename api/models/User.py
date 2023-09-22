from config.validations import validationCreateUser
#  User Class
class User:
    
    @staticmethod
    def Create(data):
        '''Create Smartsheet user'''
        try:
            # TODO: Return back sanitize data
            # display errors with the data before sending back to front end
            # if data is clean 
         validators = validationCreateUser(data)
        
         return  validators
        except Exception as e:
            # Exception thrown
            print("e",e)

        

    