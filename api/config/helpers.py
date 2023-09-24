def createTableHeaders(tableData, tableLabels):
    '''
     dynamically creates table header obj
     Name => Table label
     Value => Accessor for data key
    '''
 
    list =[]
    for x in tableData[0].keys():
        if tableLabels.get(x) is not None:
            obj ={"name": None, "value":None}
        
            obj['name']=  tableLabels.get(x)
            obj['value']= x
            list.append(obj)
        


    return list

def createFilters(queryStr):



    '''
    Dynamically creates filters and returns formatted querystring 
    '''
    print("list",queryStr)
    str = f"{queryStr.split(',')[0] if len(queryStr.split(','))   < 1 else queryStr}"
    

    return str


# Sorts collection data either ascending or desending 
def sortCollections(sort, data):
    # TODO: Fix bug
    key = sort.split(':')[0]
    value = sort.split(':')[1]
    
    

    if (value == "asc"):
        data = sorted(data, key=lambda d: d[f'{key}'])
        print(data)
        return data

    if (value == "desc"):
        data = sorted(data, key=lambda d: d[f'{key}'], reverse=True)
    return data

def searchCollection(search, searchBy, data):
   data = filter(lambda p: p[searchBy] == search, data)
   return data