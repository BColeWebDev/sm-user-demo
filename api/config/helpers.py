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