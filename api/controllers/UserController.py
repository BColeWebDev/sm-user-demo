import requests
import os
from config.credentials import API_KEY,API_URL
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
    print(pageSize)
    queryStr =""
    # builds queryParams 

    # RequireParams
    if page is None or pageSize is None:
       return {"err": "Page Number or Page Limit Missing"}, 400
    else:
       queryStr = f'?page={page}&pageSize={pageSize}'
    
    # Optionals


    resp = requests.request("GET" ,url=f"{API_URL}/users{queryStr}",headers=headers)
 
    return resp.json()
 except: 
    return  {"err":"Server Error!"},500
 
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
 
          return jsonify(createUser), 201
      
    except:
        return""

    
#  PUT - Update User 
def UpdateUser():
     '''
    GET -Update all users 
    '''
     return ""


def RemoveUser():
   '''
    GET -Remove a users 
    '''
   return ""