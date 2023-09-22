from donttrust import Schema,DontTrust
from donttrust.exceptions import DontTrustBaseException
def validationCreateUser(data):
    '''Validate incoming user data'''
    try:
     first_name = Schema().string().required()
     last_name = Schema().string().required()
     admin = Schema().boolean().required()
     licensed_sheet_creator = Schema().boolean().required()
   

     first_name.validate(data.get("first_name"))
     last_name.validate(data.get("last_name"))
     admin.validate(data.get("admin"))
     licensed_sheet_creator.validate(data.get("licensed_sheet_creator"))
   
    # Pass Validation 
     return data
    
    except DontTrustBaseException as e:
     return []