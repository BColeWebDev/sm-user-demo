import requests
import os
from config.credentials import API_KEY,API_URL
from config.helpers import createTableHeaders,createFilters
from models.User import User
from flask import request,Flask,json,jsonify
headers = {"Authorization": f"Bearer {API_KEY}"}



def AllUsers():
 
 '''
GET - Returns all users 
'''
 try:
    page = request.args.get("page")
    pageSize = request.args.get("pageSize")
    email =request.args.get("email")
    print(pageSize)
    queryStr =""
    # builds queryParams 

    # RequireParams
    if page is None or pageSize is None :
       return {"err": "Page Number or Page Limit Missing"}, 400
    else:
       
      # Query String 
     queryStr = f'?page={page}&pageSize={pageSize}{"&email={email}".format(email=createFilters(email)) if email is not None  else ""}'

    data = requests.request("GET" ,url=f"{API_URL}/users{queryStr}",headers=headers)
    response =data.json()
   
    response['tableHeaders'] = createTableHeaders(response['data'], tableLabels={"firstName":"First Name","lastName":"Last Name","id":"ID","name":"Name","email":"Email"})
    print("response",response)
    return response
 except: 
    return  {"err":"Server Error!"},500
 
def GetUser(userid):
   try: 
      
    
      if userid is None:
         return {"err":"Missing User ID"}, 400
      

      data = requests.request("GET" ,url=f"{API_URL}/users/{userid}",headers=headers)
      response =data.json()
      return response
   except:
      return ""
 
def CreateNewUser():
    '''
    GET - Returns a new user created 
    '''
    try:
         content_type = request.headers.get('Content-Type')

         if content_type != 'application/json':
             return {"err":"Content-Type not supported!"}, 400
         
         else:
          data = json.loads(request.data)
          createUser = User.Create(data={
             'first_name':data.get("first_name"),
             'last_name':data.get("last_name"),
             'email':data.get("email"),
             'admin':data.get("admin"),
             'licensed_sheet_creator':data.get("licensed_sheet_creator")
          })
          
         #  API: This operation is only available to system administrators
         # resp = requests.request("POST" ,url=f"{API_URL}/users",headers=headers, data=createUser)


         return jsonify(createUser)
      
    except:
        return""

    

