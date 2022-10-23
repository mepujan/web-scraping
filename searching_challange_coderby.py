def string_search(strArr):
    stringArray = {}
    for data in strArr:
        key,val = data.split(":")
        if stringArray.__contains__(key):
            newVal = int(stringArray.get(key)) + int(val)
            stringArray[key] = newVal
        else:
            stringArray[key] = val
    for (key, val) in stringArray.items():
        if val == 0:
            stringArray.pop(key)
    print(stringArray)
        
myArr = ['x:2','y:3','x:4','z:-1','y:-3']

string_search(myArr)