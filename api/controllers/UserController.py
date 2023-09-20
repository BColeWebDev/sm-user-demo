import requests


headers = {"Authorization": "Bearer PXvvCnSO7c6xp1c22ER1yHiD92sAwVLxonxnl"}
def AllUsers():
 resp = requests.request("GET" ,"https://api.smartsheet.com/2.0/users?page=1&pageSize=3000",headers=headers)
 print(resp)
 return resp.json()