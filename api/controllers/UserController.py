import requests
import os
from config.credentials import API_KEY,API_URL,headers
from config.helpers import createTableHeaders,createFilters,sortCollections,searchCollection
from models.User import User
from flask import request,Flask,json,jsonify

def AllUsers():
 '''
GET - Returns all users 
'''
 try:
    page = request.args.get("page")
    pageSize = request.args.get("pageSize")
    email =request.args.get("email")
    sort = request.args.get("sort")
    search = request.args.get("search")
   
   # builds queryParams
    queryStr =""


    # RequireParams
    if page is None or pageSize is None :
       return {"err": "Page Number or Page Limit Missing"}, 400
    else:
       
      # Query String 
     queryStr = f'?page={page}&pageSize={pageSize}{"&email={email}".format(email=createFilters(email)) if email is not None  else ""}'

     response = requests.request("GET" ,url=f"{API_URL}/users{queryStr}",headers=headers).json()

   #   if search is not None:
   #      response['data'] = searchCollection(search=search,searchBy="firstName",data=response)
     print(filter(lambda p: p.firstName == search,response['data']))
     if sort is not None:
        response['data'] = sortCollections(sort=sort,data=response['data'])
        

    
     response['tableHeaders'] = createTableHeaders(response['data'], tableLabels={"firstName":"First Name","lastName":"Last Name","id":"ID","name":"Name","email":"Email"})
  
    return response
 except Exception as err: 
    return  {"err":err},500
 
def GetUser(userid):
   try: 
      
    
      if userid is None:
         return {"err":"Missing User ID"}, 400
      

      data = requests.request("GET" ,url=f"{API_URL}/users/{userid}",headers=headers)
      response =data.json()
      return response
   except:
      return ""
 

