import os
# Env Variables
API_KEY = os.getenv("SM_USER_ACCESS_TOKEN")
API_URL = os.getenv("API_URL") 

headers = {"Authorization": f"Bearer {API_KEY}",
           "Content-Type":"application/json",
          }