
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
   
        return data

    if (value == "desc"):
        data = sorted(data, key=lambda d: d[f'{key}'], reverse=True)
    return data


def searchCollection(search, searchBy, data):
    '''
    Returns Sorted Collection 
    @params str search: search query string
    @params str searchBy: accessor  eg:data['email']
    @params data list[]: data set
    '''
    data =list(filter(lambda person: data if search == ""
                       or person[searchBy].lower().find(search.lower()) == -1
                       or person.get(searchBy,None) == None
                       else 
                         person[searchBy].lower().find(search.lower()) != -1, data))
    
    return data



def paginateCollection(page, pageDisplay, data):
    '''
    Returns Paginated Collection
    @params number page: page number
    @params number pageDisplay: number of pages 
    @params list[] data: data set
    '''
    startIndex = (int(page) - 1)*int(pageDisplay)
    endIndex = int(page) * int(pageDisplay)
    results = list(data[startIndex:endIndex])
    return results