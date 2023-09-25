import requests
import os
from config.credentials import API_URL,headers
from config.helpers import createTableHeaders,createFilters,sortCollections,searchCollection,paginateCollection
from models.User import User
from flask import request,Flask,json,jsonify
from math import ceil

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
     queryStr = f'?page={page}&pageSize={pageSize}&includeAll=true{"&email={email}".format(email=createFilters(email)) if email is not None  else ""}'

     response = requests.request("GET" ,url=f"{API_URL}/users{queryStr}",headers=headers).json()

     # Removes any missing names from collection 
     response['data'] = list(filter(lambda person: person if (person.get("name",None) != None or
                                    person.get("firstName",None) != None
                                    or
                                    person.get("lastName",None) != None)
                                    and 
                                    (person.get("name","") != "" or
                                    person.get("firstName","") != ""
                                    or
                                    person.get("lastName","") != "")
                                    else None ,response['data']))
      # Search Collection 
     if search is not None:
        response['data'] = searchCollection(search=search,searchBy="firstName",data=response['data'])

     response['pageNumber'] = int(page)
     response['totalPages'] = ceil(len(response['data']) / int(pageSize))

     
     
     # Sort Collection 
     if sort is not None:
        response['data'] = sortCollections(sort=sort,data=response['data'])
        
     response['data'] = paginateCollection(page=page,pageDisplay=pageSize,data=response['data'])

    
     


    
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
 

